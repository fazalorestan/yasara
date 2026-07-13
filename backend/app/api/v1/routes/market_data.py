from fastapi import APIRouter, Query, Depends
from app.market_data.application.service import market_data_service
from app.market_data.domain.models import ExchangeCode

router = APIRouter(prefix="/market-data", tags=["market-data"])

@router.get("/health")
async def exchange_health(exchange: ExchangeCode = ExchangeCode.BINANCE_FUTURES):
    return await market_data_service.health(exchange)

@router.get("/{exchange}/symbols")
async def symbols(exchange: ExchangeCode, force_refresh: bool = False):
    return await market_data_service.symbols(exchange, force_refresh=force_refresh)

@router.get("/{exchange}/ticker/{symbol:path}")
async def ticker(exchange: ExchangeCode, symbol: str):
    return await market_data_service.ticker(symbol, exchange)

@router.get("/{exchange}/candles/{symbol:path}")
async def candles(
    exchange: ExchangeCode,
    symbol: str,
    timeframe: str = "15m",
    limit: int = Query(default=500, ge=1, le=1500),
):
    return await market_data_service.candles(symbol, timeframe, limit, exchange)

@router.get("/{exchange}/order-book/{symbol:path}")
async def order_book(
    exchange: ExchangeCode,
    symbol: str,
    limit: int = Query(default=100, ge=5, le=1000),
):
    return await market_data_service.order_book(symbol, limit, exchange)

@router.get("/{exchange}/funding-rate/{symbol:path}")
async def funding_rate(exchange: ExchangeCode, symbol: str):
    return await market_data_service.funding_rate(symbol, exchange)

@router.get("/{exchange}/open-interest/{symbol:path}")
async def open_interest(exchange: ExchangeCode, symbol: str):
    return await market_data_service.open_interest(symbol, exchange)


from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session
from app.market_data.application.realtime_service import realtime_market_data_service
from app.market_data.application.sync_service import market_data_sync_service

class RealtimeStartRequest(BaseModel):
    symbols: list[str]
    timeframes: list[str] = ["1m"]

@router.post("/realtime/binance/start")
async def start_binance_realtime(payload: RealtimeStartRequest):
    return await realtime_market_data_service.start_binance(payload.symbols, payload.timeframes)

@router.post("/realtime/binance/stop")
async def stop_binance_realtime():
    return await realtime_market_data_service.stop_binance()

@router.get("/realtime/stats")
async def realtime_stats():
    return realtime_market_data_service.stats()

@router.post("/{exchange}/sync-candles/{symbol:path}")
async def sync_candles(exchange: ExchangeCode, symbol: str, session = None, timeframe: str = "15m", limit: int = Query(default=500, ge=1, le=1500)):
    # Database session injection will be wired to the repository layer in the application deployment.
    # This endpoint is intentionally disabled without DI session to avoid silent writes.
    return {"status": "requires_database_session", "exchange": exchange.value, "symbol": symbol, "timeframe": timeframe, "limit": limit}

from app.market_data.application.scheduler import market_data_scheduler, SyncJobConfig


@router.post("/{exchange}/sync-candles-db/{symbol:path}")
async def sync_candles_db(
    exchange: ExchangeCode,
    symbol: str,
    session: AsyncSession = Depends(get_db_session),
    timeframe: str = "15m",
    limit: int = Query(default=500, ge=1, le=1500),
):
    return await market_data_sync_service.sync_candles(session, symbol, timeframe, limit, exchange)

@router.get("/{exchange}/stored-candles/{symbol:path}")
async def stored_candles(
    exchange: ExchangeCode,
    symbol: str,
    session: AsyncSession = Depends(get_db_session),
    timeframe: str = "15m",
    limit: int = Query(default=500, ge=1, le=1500),
):
    return await market_data_sync_service.stored_candles(session, symbol, timeframe, limit, exchange)

@router.get("/{exchange}/gaps/{symbol:path}")
async def candle_gaps(
    exchange: ExchangeCode,
    symbol: str,
    session: AsyncSession = Depends(get_db_session),
    timeframe: str = "15m",
    limit: int = Query(default=1000, ge=10, le=5000),
):
    return await market_data_sync_service.detect_gaps(session, symbol, timeframe, exchange, limit)

@router.post("/{exchange}/repair-gap/{symbol:path}")
async def repair_latest_gap(
    exchange: ExchangeCode,
    symbol: str,
    session: AsyncSession = Depends(get_db_session),
    timeframe: str = "15m",
):
    return await market_data_sync_service.repair_latest_gap(session, symbol, timeframe, exchange)

class SyncJobRequest(BaseModel):
    symbol: str
    timeframe: str = "15m"
    seconds: int = 60
    limit: int = 500
    exchange: ExchangeCode = ExchangeCode.BINANCE_FUTURES

@router.post("/scheduler/jobs")
async def add_scheduler_job(payload: SyncJobRequest):
    job_id = market_data_scheduler.add_sync_job(
        SyncJobConfig(symbol=payload.symbol, timeframe=payload.timeframe, limit=payload.limit, exchange=payload.exchange),
        seconds=payload.seconds,
    )
    return {"job_id": job_id, "scheduler": market_data_scheduler.stats()}

@router.delete("/scheduler/jobs/{job_id:path}")
async def remove_scheduler_job(job_id: str):
    return {"removed": market_data_scheduler.remove_job(job_id), "scheduler": market_data_scheduler.stats()}

@router.get("/scheduler/stats")
async def scheduler_stats():
    return market_data_scheduler.stats()
