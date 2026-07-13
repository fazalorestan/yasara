from fastapi import APIRouter
from app.v22_market_engine.service import MarketDataEngineServiceV22

router = APIRouter(prefix="/v2-2/market-engine", tags=["v2.2-market-engine"])
_service = MarketDataEngineServiceV22()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/tick")
async def tick(symbol: str = "BTCUSDT", exchange: str = "binance"):
    return _service.tick(symbol, exchange)

@router.get("/ohlc")
async def ohlc(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "4H", limit: int = 120):
    return _service.ohlc(symbol, exchange, timeframe, limit)

@router.get("/snapshot")
async def snapshot(exchange: str = "all"):
    return _service.snapshot(exchange)
