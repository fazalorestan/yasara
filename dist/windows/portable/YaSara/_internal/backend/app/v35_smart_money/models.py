from pydantic import BaseModel, Field


class SmartMoneySummaryV35(BaseModel):
    ready: bool = True
    phase: str = "v3_5_smart_money_engine_core"
    product_progress_percent: int = 78
    remaining_to_professional_product_percent: int = 22
    constitution_compliant: bool = True
    safety: str = "analysis_only_live_trading_disabled"


class SmartMoneyRequestV35(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    limit: int = 160
    feature_flags: dict = Field(default_factory=lambda: {
        "order_block": True,
        "bos": True,
        "choch": True,
        "liquidity_sweep": True,
        "liquidity_grab": True,
        "fair_value_gap": True,
        "imbalance": True,
        "premium_discount": True,
        "equal_high_low": True,
    })
