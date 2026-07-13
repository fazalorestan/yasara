from pydantic import BaseModel, Field


class IndicatorEngineSummaryV41(BaseModel):
    ready: bool = True
    phase: str = "v4_1_modular_indicator_engine_foundation"
    product_progress_percent: int = 88
    remaining_to_professional_product_percent: int = 12
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "analysis_only_live_trading_disabled"


class IndicatorRequestV41(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    limit: int = 160
    indicators: list[str] = Field(default_factory=lambda: [
        "ema", "sma", "rsi", "macd", "atr", "adx", "supertrend",
        "vwap", "bollinger", "obv", "mfi", "cci", "stochastic",
        "donchian", "keltner", "parabolic_sar"
    ])


class IndicatorResultV41(BaseModel):
    name: str
    ready: bool = True
    value: dict
    confidence: float = 50
    bias: str = "neutral"
