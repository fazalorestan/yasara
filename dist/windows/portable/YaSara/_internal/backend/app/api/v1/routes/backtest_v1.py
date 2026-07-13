from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.backtest_v1.application.service import backtest_service_v1
from app.backtest_v1.domain.models import BacktestConfig
from app.core.database import get_db_session
from app.market_data.domain.models import ExchangeCode

router = APIRouter(prefix="/backtest-v1", tags=["backtest-v1"])

@router.post("/{exchange}/live")
async def run_live(exchange: ExchangeCode, config: BacktestConfig, limit: int = Query(default=1000, ge=100, le=1500)):
    return await backtest_service_v1.run_live(exchange, config, limit)

@router.post("/{exchange}/stored")
async def run_stored(
    exchange: ExchangeCode,
    config: BacktestConfig,
    session: AsyncSession = Depends(get_db_session),
    limit: int = Query(default=1000, ge=100, le=5000),
):
    return await backtest_service_v1.run_stored(session, exchange, config, limit)

@router.post("/{exchange}/monte-carlo/live")
async def monte_carlo_live(
    exchange: ExchangeCode,
    config: BacktestConfig,
    limit: int = Query(default=1000, ge=100, le=1500),
    simulations: int = Query(default=500, ge=50, le=5000),
):
    return await backtest_service_v1.monte_carlo_live(exchange, config, limit, simulations)

@router.post("/{exchange}/walk-forward/live")
async def walk_forward_live(exchange: ExchangeCode, config: BacktestConfig, limit: int = Query(default=1500, ge=500, le=1500)):
    return await backtest_service_v1.walk_forward_live(exchange, config, limit)
