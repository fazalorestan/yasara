from pydantic import BaseModel, Field

class SmartMoneyProSummaryV411(BaseModel):
    ready: bool = True
    phase: str = "v4_11_smart_money_professional_sprint_1"
    analysis_progress_percent: int = 87
    remaining_to_final_professional_analysis_percent: int = 13
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "analysis_only_no_real_execution"

class SmartMoneyProRequestV411(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    limit: int = 180
    feature_flags: dict = Field(default_factory=lambda: {
        "order_block_pro": True,
        "fair_value_gap_pro": True,
        "imbalance": True,
        "mitigation": True,
        "breaker_candidate": True,
        "structure_integration": True,
    })
