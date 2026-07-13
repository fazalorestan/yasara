from pydantic import BaseModel

class AIRecommendationInputV1(BaseModel):
    direction: str
    confidence: float
    risk_approved: bool

class AIRecommendationV1(BaseModel):
    action: str
    message: str

class AIRecommendationEngineV1:
    def recommend(self, item: AIRecommendationInputV1) -> AIRecommendationV1:
        if not item.risk_approved:
            return AIRecommendationV1(action="wait", message="Risk rejected the setup.")
        if item.confidence >= 75 and item.direction in {"long", "short"}:
            return AIRecommendationV1(action=item.direction, message="Setup is actionable in paper trading.")
        return AIRecommendationV1(action="wait", message="Confidence is not strong enough.")
