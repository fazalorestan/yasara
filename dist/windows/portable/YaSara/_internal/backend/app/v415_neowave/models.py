from pydantic import BaseModel, Field

class NeoWaveSummaryV415(BaseModel):
    ready: bool = True
    phase: str = "v4_15_neowave_engine_sprint_1"
    analysis_progress_percent: int = 78
    remaining_to_final_professional_analysis_percent: int = 22
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "analysis_only_no_real_execution"

class NeoWaveRequestV415(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    limit: int = 180
    pivot_left: int = 2
    pivot_right: int = 2
    feature_flags: dict = Field(default_factory=lambda: {
        "wave_model": True,
        "wave_validation": True,
        "pattern_skeleton": True,
        "rule_registry": True,
        "context_score": True,
    })
