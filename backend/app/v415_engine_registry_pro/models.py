from pydantic import BaseModel, Field

class EngineRegistryProSummaryV415(BaseModel):
    ready: bool = True
    phase: str = "v4_15_engine_registry_pro_neowave_sprint_1"
    analysis_progress_percent: int = 78
    remaining_to_final_professional_analysis_percent: int = 22
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "analysis_only_no_real_execution"

class EngineOutputContractV415(BaseModel):
    engine: str
    version: str = "v4.15"
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    bias: str = "neutral"
    confidence: float = 50
    reasons: list[str] = Field(default_factory=list)
    payload: dict = Field(default_factory=dict)
    real_order_execution_enabled: bool = False
    live_trading_enabled: bool = False
