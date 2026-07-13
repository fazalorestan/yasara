from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/v2-5/risk-backtest-paper", tags=["v2.5-risk-backtest-paper"])


class RiskBacktestPaperSummary(BaseModel):
    ready: bool = True
    status: str = "not_yet_run"


class BacktestResult(BaseModel):
    ready: bool = True
    symbol: str
    exchange: str
    timeframe: str
    portfolio_var_95: float = 0.0
    max_drawdown_percent: float = 0.0
    sharpe_ratio: float = 0.0
    win_rate_percent: float = 0.0
    total_return_percent: float = 0.0
    equity_curve: List[float] = [0.0, 0.0]


class PaperOrder(BaseModel):
    symbol: str
    side: str
    type: str = "LIMIT"
    qty: float = 0.0
    price: float = 0.0
    status: str = "OPEN"


class PaperState(BaseModel):
    ready: bool = True
    orders: List[PaperOrder] = []
    total_return_percent: float = 0.0
    equity_curve: List[float] = [0.0, 0.0]


@router.get("/summary", response_model=RiskBacktestPaperSummary)
async def summary() -> RiskBacktestPaperSummary:
    return RiskBacktestPaperSummary()


@router.get("/backtest", response_model=BacktestResult)
async def backtest(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "4H") -> BacktestResult:
    return BacktestResult(symbol=symbol, exchange=exchange, timeframe=timeframe)


@router.get("/paper-state", response_model=PaperState)
async def paper_state() -> PaperState:
    return PaperState()
