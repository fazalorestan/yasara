from pydantic import BaseModel

class ConfidenceFactorsV1(BaseModel):
    signal_quality: float
    liquidity_score: float
    risk_penalty: float = 0
    data_quality: float = 100

class ConfidenceEngineV1:
    def calculate(self, factors: ConfidenceFactorsV1) -> float:
        score = factors.signal_quality * 0.4 + factors.liquidity_score * 0.25 + factors.data_quality * 0.25 - factors.risk_penalty * 0.1
        return max(0, min(100, score))
