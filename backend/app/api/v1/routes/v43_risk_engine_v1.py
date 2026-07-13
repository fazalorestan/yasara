from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/v4-3/risk-engine", tags=["v4.3-risk-engine"])


class RiskEngineSummary(BaseModel):
    ready: bool = True
    risk_level: str = "Low"
    exposure_percent: float = 0.0


class SignalRisk(BaseModel):
    ready: bool = True
    symbol: str
    exchange: str
    timeframe: str
    risk_level: str = "Low"
    risk_score: float = 0.0


@router.get("/summary", response_model=RiskEngineSummary)
async def summary() -> RiskEngineSummary:
    return RiskEngineSummary()


@router.get("/signal-risk", response_model=SignalRisk)
async def signal_risk(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m") -> SignalRisk:
    return SignalRisk(symbol=symbol, exchange=exchange, timeframe=timeframe)
