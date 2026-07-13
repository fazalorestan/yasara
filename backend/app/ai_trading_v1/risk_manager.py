from pydantic import BaseModel

class AIRiskInputV1(BaseModel):
    signal_confidence: float
    volatility_percent: float
    portfolio_risk_score: float

class AIRiskResultV1(BaseModel):
    approved: bool
    risk_level: str
    recommendation: str

class AIRiskManagerV1:
    def evaluate(self, item: AIRiskInputV1) -> AIRiskResultV1:
        composite = item.portfolio_risk_score + item.volatility_percent * 3 - item.signal_confidence * 0.2
        if composite >= 80:
            return AIRiskResultV1(approved=False, risk_level="critical", recommendation="block_trade")
        if composite >= 50:
            return AIRiskResultV1(approved=True, risk_level="warning", recommendation="reduce_size")
        return AIRiskResultV1(approved=True, risk_level="ok", recommendation="normal_size")
