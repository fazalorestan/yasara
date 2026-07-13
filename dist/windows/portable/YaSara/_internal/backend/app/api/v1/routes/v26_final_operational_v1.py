from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/v2-6/final-operational", tags=["v2.6-final-operational"])


class FinalOperationalSummary(BaseModel):
    ready: bool = True
    status: str = "operational"
    modules_online: int = 0


class FinalOperationalHealth(BaseModel):
    ready: bool = True
    latency_ms: int = 0
    data_rate_mbps: float = 0.0
    connections: int = 0
    cpu_percent: int = 0
    memory_percent: int = 0
    disk_percent: int = 0
    uptime: str = "0m"
    mode: str = "Mode: Safe · Paper Trading Only"


class FinalOperationalModules(BaseModel):
    ready: bool = True
    modules: List[str] = []


class FinalOperationalDashboard(BaseModel):
    ready: bool = True
    symbol: str
    exchange: str
    timeframe: str


class FinalOperationalReleaseGate(BaseModel):
    ready: bool = True
    score: float = 0.0
    execution_allowed: bool = False


@router.get("/summary", response_model=FinalOperationalSummary)
async def summary() -> FinalOperationalSummary:
    return FinalOperationalSummary()


@router.get("/health", response_model=FinalOperationalHealth)
async def health() -> FinalOperationalHealth:
    return FinalOperationalHealth()


@router.get("/modules", response_model=FinalOperationalModules)
async def modules() -> FinalOperationalModules:
    return FinalOperationalModules()


@router.get("/dashboard", response_model=FinalOperationalDashboard)
async def dashboard(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "4H") -> FinalOperationalDashboard:
    return FinalOperationalDashboard(symbol=symbol, exchange=exchange, timeframe=timeframe)


@router.get("/release-gate", response_model=FinalOperationalReleaseGate)
async def release_gate() -> FinalOperationalReleaseGate:
    return FinalOperationalReleaseGate()
