from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session
from app.intelligence_v1.application.service import market_intelligence_service_v1
from app.market_data.domain.models import ExchangeCode

router = APIRouter(prefix="/intelligence-v1", tags=["intelligence-v1"])

@router.get("/{exchange}/live/{symbol:path}")
async def analyze_live(
    exchange: ExchangeCode,
    symbol: str,
    timeframes: list[str] = Query(default=["15m", "1h", "4h"]),
    limit: int = Query(default=250, ge=60, le=1000),
):
    return await market_intelligence_service_v1.analyze_live(exchange, symbol, timeframes, limit)

@router.get("/{exchange}/stored/{symbol:path}")
async def analyze_stored(
    exchange: ExchangeCode,
    symbol: str,
    session: AsyncSession = Depends(get_db_session),
    timeframes: list[str] = Query(default=["15m", "1h", "4h"]),
    limit: int = Query(default=250, ge=60, le=1000),
):
    return await market_intelligence_service_v1.analyze_stored(session, exchange, symbol, timeframes, limit)
