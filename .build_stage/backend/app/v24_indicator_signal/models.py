from pydantic import BaseModel


class IndicatorSummaryV24(BaseModel):
    ready: bool = True
    phase: str = "v2_4_indicator_signal_engine_activation"
    operational_progress_percent: int = 93
    remaining_to_full_operational_percent: int = 7
    safety: str = "analysis_only_live_trading_disabled"


class IndicatorSnapshotV24(BaseModel):
    symbol: str
    exchange: str
    timeframe: str
    ema_fast: float
    ema_slow: float
    rsi: float
    macd: float
    macd_signal: float
    trend: str
    signal: str
    confidence: int
