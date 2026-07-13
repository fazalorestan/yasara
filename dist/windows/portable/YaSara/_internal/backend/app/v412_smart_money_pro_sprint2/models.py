from pydantic import BaseModel, Field

class SmartMoneyProSprint2SummaryV412(BaseModel):
    ready: bool = True
    phase: str = "v4_12_smart_money_professional_sprint_2"
    analysis_progress_percent: int = 90
    remaining_to_final_professional_analysis_percent: int = 10
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "analysis_only_no_real_execution"

class SmartMoneyProSprint2RequestV412(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    limit: int = 180
    feature_flags: dict = Field(default_factory=lambda: {
        "liquidity_grab": True,
        "sweep_pro": True,
        "equal_level_integration": True,
        "premium_discount_entry": True,
        "ob_fvg_confluence": True,
        "entry_quality_score": True,
    })
