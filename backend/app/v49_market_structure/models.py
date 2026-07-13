from pydantic import BaseModel, Field


class MarketStructureSummaryV49(BaseModel):
    ready: bool = True
    phase: str = "v4_9_professional_market_structure_sprint_1"
    product_progress_percent: int = 81
    remaining_to_final_professional_analysis_percent: int = 19
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "analysis_only_no_real_execution"


class MarketStructureRequestV49(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    limit: int = 180
    pivot_left: int = 2
    pivot_right: int = 2
    feature_flags: dict = Field(default_factory=lambda: {
        "swings": True,
        "bos": True,
        "choch": True,
        "trend_state": True,
        "range_state": True,
        "premium_discount": True,
        "context_score": True,
    })
