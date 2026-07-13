from pydantic import BaseModel


class AdvancedAIIndicatorSummaryV32(BaseModel):
    ready: bool = True
    phase: str = "v3_2_advanced_ai_indicator_engine"
    product_progress_percent: int = 57
    remaining_to_professional_product_percent: int = 43
    safety: str = "analysis_only_live_trading_disabled"


class AdvancedIndicatorRequestV32(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    limit: int = 120
