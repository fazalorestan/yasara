from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/v4-14/ai-fusion", tags=["v4.14-ai-fusion"])


class AIFusionSummary(BaseModel):
    ready: bool = True
    decision: str = "WAIT"
    confidence: float = 0.0
    bias: str = "Neutral"
    strength: str = "--"
    timeframe: str = "4H"
    strategy: str = "--"
    risk_level: str = "Low"
    recommendation: str = "No signal generated yet."
    key_level: Optional[str] = None


class AIFusionQuick(BaseModel):
    ready: bool = True
    symbol: str
    exchange: str
    timeframe: str
    decision: str = "WAIT"
    confidence: float = 0.0


@router.get("/summary", response_model=AIFusionSummary)
async def summary() -> AIFusionSummary:
    return AIFusionSummary()


@router.get("/quick", response_model=AIFusionQuick)
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m") -> AIFusionQuick:
    return AIFusionQuick(symbol=symbol, exchange=exchange, timeframe=timeframe)
