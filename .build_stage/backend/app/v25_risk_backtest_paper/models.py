from pydantic import BaseModel


class RiskBacktestPaperSummaryV25(BaseModel):
    ready: bool = True
    phase: str = "v2_5_risk_backtest_paper_activation"
    operational_progress_percent: int = 98
    remaining_to_full_operational_percent: int = 2
    safety: str = "paper_trading_only_live_trading_disabled"


class PaperOrderV25(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    side: str = "buy"
    quantity: float = 0.01
    order_type: str = "market"


class RiskRequestV25(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    equity: float = 10000
    risk_percent: float = 1.0
    stop_distance_percent: float = 2.0
