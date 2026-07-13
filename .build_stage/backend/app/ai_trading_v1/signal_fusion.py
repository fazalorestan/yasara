from pydantic import BaseModel

class SignalInputV1(BaseModel):
    source: str
    direction: str
    confidence: float
    weight: float = 1.0

class SignalFusionResultV1(BaseModel):
    direction: str
    confidence: float
    sources: int

class SignalFusionEngineV1:
    def fuse(self, signals: list[SignalInputV1]) -> SignalFusionResultV1:
        if not signals:
            return SignalFusionResultV1(direction="wait", confidence=0, sources=0)
        long_score = sum(s.confidence * s.weight for s in signals if s.direction == "long")
        short_score = sum(s.confidence * s.weight for s in signals if s.direction == "short")
        total_weight = sum(s.weight for s in signals) or 1
        if long_score > short_score:
            return SignalFusionResultV1(direction="long", confidence=min(100, long_score / total_weight), sources=len(signals))
        if short_score > long_score:
            return SignalFusionResultV1(direction="short", confidence=min(100, short_score / total_weight), sources=len(signals))
        return SignalFusionResultV1(direction="wait", confidence=0, sources=len(signals))
