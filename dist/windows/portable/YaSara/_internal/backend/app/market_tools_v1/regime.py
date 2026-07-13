from enum import StrEnum
from pydantic import BaseModel

class MarketRegime(StrEnum):
    TRENDING_UP = "trending_up"
    TRENDING_DOWN = "trending_down"
    RANGE = "range"

class MarketRegimeResultV1(BaseModel):
    regime: MarketRegime
    score: float

class MarketRegimeDetectorV1:
    def detect(self, closes: list[float]) -> MarketRegimeResultV1:
        if len(closes) < 2:
            return MarketRegimeResultV1(regime=MarketRegime.RANGE, score=0)
        change = closes[-1] - closes[0]
        pct = change / closes[0] * 100 if closes[0] else 0
        if pct > 2:
            return MarketRegimeResultV1(regime=MarketRegime.TRENDING_UP, score=pct)
        if pct < -2:
            return MarketRegimeResultV1(regime=MarketRegime.TRENDING_DOWN, score=abs(pct))
        return MarketRegimeResultV1(regime=MarketRegime.RANGE, score=abs(pct))
