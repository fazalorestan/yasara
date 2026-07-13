from pydantic import BaseModel

class LiquidityInputV1(BaseModel):
    volume: float
    spread_percent: float

class LiquidityScoreV1(BaseModel):
    score: float
    level: str

class LiquidityScoreEngineV1:
    def score(self, item: LiquidityInputV1) -> LiquidityScoreV1:
        volume_score = min(70, item.volume / 1000 * 70)
        spread_penalty = min(50, item.spread_percent * 10)
        score = max(0, min(100, volume_score + 30 - spread_penalty))
        level = "high" if score >= 70 else "medium" if score >= 40 else "low"
        return LiquidityScoreV1(score=score, level=level)
