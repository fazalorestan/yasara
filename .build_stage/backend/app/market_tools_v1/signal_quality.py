from pydantic import BaseModel

class SignalQualityInputV1(BaseModel):
    confidence: float
    liquidity_score: float
    volatility_percent: float

class SignalQualityResultV1(BaseModel):
    quality: float
    grade: str

class SignalQualityEngineV1:
    def evaluate(self, item: SignalQualityInputV1) -> SignalQualityResultV1:
        volatility_penalty = min(30, item.volatility_percent * 2)
        quality = max(0, min(100, item.confidence * 0.6 + item.liquidity_score * 0.4 - volatility_penalty))
        grade = "A" if quality >= 80 else "B" if quality >= 60 else "C" if quality >= 40 else "D"
        return SignalQualityResultV1(quality=quality, grade=grade)
