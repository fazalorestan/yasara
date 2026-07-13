from pydantic import BaseModel, Field

class NeoWaveSprint2SummaryV416(BaseModel):
    ready: bool = True
    phase: str = "v4_16_neowave_engine_sprint_2"
    analysis_progress_percent: int = 82
    remaining_to_final_professional_analysis_percent: int = 18
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "analysis_only_no_real_execution"

class NeoWaveSprint2RequestV416(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    limit: int = 180
    feature_flags: dict = Field(default_factory=lambda: {
        "complexity": True,
        "time_rules": True,
        "price_rules": True,
        "ratio_analysis": True,
        "pattern_confidence": True,
        "fusion_ready_output": True,
    })
