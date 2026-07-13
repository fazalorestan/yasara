from pydantic import BaseModel

class MarketTickV22(BaseModel):
    symbol: str
    exchange: str
    price: float
    spread: float
    source: str = "v22_market_engine"

class OhlcCandleV22(BaseModel):
    time: int
    open: float
    high: float
    low: float
    close: float
    volume: float

class OhlcResponseV22(BaseModel):
    ready: bool = True
    symbol: str
    exchange: str
    timeframe: str
    candles: list[OhlcCandleV22]
    source: str = "v22_market_engine_demo_adapter"

class MarketEngineSummaryV22(BaseModel):
    ready: bool = True
    phase: str = "v2_2_market_data_engine_phase_1"
    operational_progress_percent: int = 75
    remaining_to_full_operational_percent: int = 25
    safety: str = "market_data_only_live_trading_disabled"
