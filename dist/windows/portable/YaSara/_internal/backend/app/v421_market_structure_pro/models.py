from pydantic import BaseModel, Field

class MarketStructureProSummaryV421(BaseModel):
    ready: bool = True
    phase: str = "v4_21_professional_market_structure_engine_sprint_3"
    scope: str = "analysis_engine"
    analysis_progress_percent: int = 84
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "analysis_only_no_real_execution"

class MarketStructureProRequestV421(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "15m"
    limit: int = 240
    pivot_left: int = 2
    pivot_right: int = 2
    range_tolerance_percent: float = 0.35
    feature_flags: dict = Field(default_factory=lambda: {
        "confirmed_swings": True,
        "bos": True,
        "choch": True,
        "trend_state": True,
        "range_state": True,
        "chart_annotations": True,
        "fusion_ready_output": True,
    })
