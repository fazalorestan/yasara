from pydantic import BaseModel, Field

class ElliottSummaryV417(BaseModel):
    ready: bool = True
    phase: str = "v4_17_elliott_wave_engine_sprint_1"
    analysis_progress_percent: int = 80
    remaining_to_final_professional_analysis_percent: int = 20
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "analysis_only_no_real_execution"

class ElliottRequestV417(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    limit: int = 180
    pivot_left: int = 2
    pivot_right: int = 2
    feature_flags: dict = Field(default_factory=lambda: {
        "wave_parser": True,
        "wave_numbering": True,
        "impulse_skeleton": True,
        "correction_skeleton": True,
        "basic_rules": True,
        "fibonacci_base": True,
        "invalid_count": True,
    })
