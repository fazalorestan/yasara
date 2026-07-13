from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session
from app.decision_v1.application.service import decision_service_v1
from app.market_data.domain.models import ExchangeCode

router = APIRouter(prefix="/decision-v1", tags=["decision-v1"])

class RankRequest(BaseModel):
    symbols: list[str] = Field(..., min_length=1, max_length=50)
    timeframes: list[str] = ["15m", "1h", "4h"]
    limit: int = 250

@router.get("/{exchange}/live/{symbol:path}")
async def decide_live(
    exchange: ExchangeCode,
    symbol: str,
    timeframes: list[str] = Query(default=["15m", "1h", "4h"]),
    limit: int = Query(default=250, ge=60, le=1000),
):
    return await decision_service_v1.decide_live(exchange, symbol, timeframes, limit)

@router.get("/{exchange}/stored/{symbol:path}")
async def decide_stored(
    exchange: ExchangeCode,
    symbol: str,
    session: AsyncSession = Depends(get_db_session),
    timeframes: list[str] = Query(default=["15m", "1h", "4h"]),
    limit: int = Query(default=250, ge=60, le=1000),
):
    return await decision_service_v1.decide_stored(session, exchange, symbol, timeframes, limit)

@router.post("/{exchange}/rank/live")
async def rank_live(exchange: ExchangeCode, payload: RankRequest):
    return await decision_service_v1.rank_live(exchange, payload.symbols, payload.timeframes, payload.limit)
