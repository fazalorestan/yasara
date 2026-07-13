from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class BacktestConfig:
    strategy_id: str
    symbol: str
    timeframe: str = "1h"
    initial_equity: float = 10000.0
    fee_pct: float = 0.1
    slippage_pct: float = 0.05
    risk_pct: float = 1.0

@dataclass
class HistoricalCandle:
    timestamp: str
    open: float
    high: float
    low: float
    close: float
    volume: float

@dataclass
class SimulatedTrade:
    symbol: str
    side: str
    entry_price: float
    exit_price: float
    quantity: float
    pnl: float
    metadata: dict[str, Any] = field(default_factory=dict)
    closed_at: str = field(default_factory=utc_now_iso)

@dataclass
class BacktestReport:
    ready: bool
    total_trades: int
    net_pnl: float
    win_rate: float
    max_drawdown_pct: float
