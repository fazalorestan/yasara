from pydantic import BaseModel, Field
from app.v11_ai_market_intelligence.service import AIMarketIntelligenceServiceV11


class V11Phase3Summary(BaseModel):
    ready: bool
    phase: str = "v1_1_phase_3_ai_market_intelligence"
    capabilities: list[str] = Field(default_factory=list)
    safety: str = "analysis_only_no_live_trading"


class V11Phase3SummaryBuilder:
    def build(self) -> V11Phase3Summary:
        payload = AIMarketIntelligenceServiceV11().dashboard_payload()
        return V11Phase3Summary(
            ready=payload["ready"] and payload["count"] >= 1,
            capabilities=[
                "feature_builder",
                "market_regime_detector",
                "ai_risk_classifier",
                "signal_scorer",
                "insight_engine",
                "dashboard_payload",
            ],
        )
