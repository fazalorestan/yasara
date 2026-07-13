from dataclasses import dataclass

@dataclass
class RiskPolicy:
    max_risk_per_trade_pct: float = 1.0
    max_daily_loss_pct: float = 3.0
    max_drawdown_pct: float = 10.0
    max_symbol_exposure_pct: float = 20.0
    max_portfolio_exposure_pct: float = 60.0
    live_execution_allowed: bool = False
    auto_trading_allowed: bool = False

@dataclass
class PositionSizeRequest:
    account_equity: float
    risk_pct: float
    entry_price: float
    stop_loss_price: float

@dataclass
class RiskDecision:
    allowed: bool
    reason: str
    score: float = 0.0
    execution_allowed: bool = False
