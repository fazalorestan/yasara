from pydantic import BaseModel, Field

class MarketStructureSprint2SummaryV410(BaseModel):
    ready: bool = True
    phase: str = "v4_10_market_structure_engine_sprint_2"
    analysis_progress_percent: int = 84
    remaining_to_final_professional_analysis_percent: int = 16
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "analysis_only_no_real_execution"

class MarketStructureSprint2RequestV410(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframes: list[str] = Field(default_factory=lambda: ["1m", "5m", "15m", "1h"])
    limit: int = 180
    equal_tolerance_percent: float = 0.08
