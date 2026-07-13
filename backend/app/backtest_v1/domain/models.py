from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field
from app.decision_v1.domain.models import DecisionDirection

class BacktestMode(StrEnum):
    CANDLE_REPLAY = "candle_replay"
    HISTORICAL_DECISION = "historical_decision"

class TradeStatus(StrEnum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"

class ExitReason(StrEnum):
    TAKE_PROFIT = "take_profit"
    STOP_LOSS = "stop_loss"
    END_OF_TEST = "end_of_test"
    NO_EXIT = "no_exit"

class CostModel(BaseModel):
    commission_rate: float = 0.0004
    slippage_rate: float = 0.0002
    funding_rate_per_8h: float = 0.0001

class BacktestConfig(BaseModel):
    exchange: str = "binance_futures"
    symbol: str
    timeframe: str = "15m"
    initial_capital: float = 10000
    risk_per_trade_pct: float = 1.0
    leverage: float = 1.0
    max_open_trades: int = 1
    cost_model: CostModel = Field(default_factory=CostModel)

class BacktestTrade(BaseModel):
    id: str
    symbol: str
    direction: DecisionDirection
    entry_time: datetime
    entry_price: float
    quantity: float
    stop_loss: float
    take_profit: float
    exit_time: datetime | None = None
    exit_price: float | None = None
    status: TradeStatus = TradeStatus.OPEN
    exit_reason: ExitReason = ExitReason.NO_EXIT
    gross_pnl: float = 0
    fees: float = 0
    slippage: float = 0
    funding: float = 0
    net_pnl: float = 0
    return_pct: float = 0

class EquityPoint(BaseModel):
    time: datetime
    equity: float
    drawdown_pct: float = 0

class BacktestMetrics(BaseModel):
    total_trades: int = 0
    wins: int = 0
    losses: int = 0
    win_rate: float = 0
    gross_profit: float = 0
    gross_loss: float = 0
    net_profit: float = 0
    net_profit_pct: float = 0
    profit_factor: float = 0
    expectancy: float = 0
    max_drawdown_pct: float = 0
    recovery_factor: float = 0
    sharpe_proxy: float = 0
    average_win: float = 0
    average_loss: float = 0

class BacktestReport(BaseModel):
    config: BacktestConfig
    metrics: BacktestMetrics
    trades: list[BacktestTrade]
    equity_curve: list[EquityPoint]
    warnings: list[str] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class WalkForwardWindow(BaseModel):
    train_start: datetime
    train_end: datetime
    test_start: datetime
    test_end: datetime
    report: BacktestReport | None = None

class MonteCarloResult(BaseModel):
    simulations: int
    median_final_equity: float
    worst_final_equity: float
    best_final_equity: float
    risk_of_ruin_pct: float
