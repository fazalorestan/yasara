from pydantic import BaseModel, Field

class ICTEngineSummaryV413(BaseModel):
    ready: bool = True
    phase: str = "v4_13_ict_engine_sprint_1"
    analysis_progress_percent: int = 92
    remaining_to_final_professional_analysis_percent: int = 8
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "analysis_only_no_real_execution"

class ICTEngineRequestV413(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    limit: int = 180
    feature_flags: dict = Field(default_factory=lambda: {
        "kill_zones": True,
        "judas_swing": True,
        "power_of_three": True,
        "ote": True,
        "liquidity_model": True,
        "ict_context_score": True,
    })
