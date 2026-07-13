from pydantic import BaseModel, Field

class AIDecisionFusionSummaryV414(BaseModel):
    ready: bool = True
    phase: str = "v4_14_ai_decision_fusion_engine_sprint_1"
    analysis_progress_percent: int = 94
    remaining_to_final_professional_analysis_percent: int = 6
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "decision_analysis_only_no_real_execution"

class AIDecisionFusionRequestV414(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    limit: int = 180
    feature_flags: dict = Field(default_factory=lambda: {
        "market_context": True,
        "market_structure": True,
        "smart_money": True,
        "ict": True,
        "indicator": True,
        "risk": True,
        "fusion": True,
        "explanation": True,
    })
