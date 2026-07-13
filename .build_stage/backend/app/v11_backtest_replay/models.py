from pydantic import BaseModel, Field
from time import time


class ReplayCandleV11(BaseModel):
    symbol: str
    timestamp: float
    open: float
    high: float
    low: float
    close: float
    volume: float = 0.0


class ReplayDatasetV11(BaseModel):
    symbol: str
    candles: list[ReplayCandleV11] = Field(default_factory=list)


class BacktestTradeV11(BaseModel):
    symbol: str
    action: str
    price: float
    quantity: float
    timestamp: float
    reason: str = ""


class BacktestMetricsV11(BaseModel):
    total_trades: int = 0
    winning_trades: int = 0
    losing_trades: int = 0
    realized_pnl: float = 0.0
    max_drawdown: float = 0.0
    final_equity: float = 10000.0


class BacktestRunResultV11(BaseModel):
    ready: bool
    symbol: str
    trades: list[BacktestTradeV11] = Field(default_factory=list)
    metrics: BacktestMetricsV11
    safety: str = "backtest_only_no_live_execution"
    completed_at: float = Field(default_factory=time)
