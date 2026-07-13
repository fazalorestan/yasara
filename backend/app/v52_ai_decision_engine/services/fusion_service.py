from app.v52_ai_decision_engine.models import DecisionDirection, DecisionResult, EvidenceStatus, FusionRequest

class FusionService:
    def fuse(self, request: FusionRequest) -> DecisionResult:
        confirmed = [e for e in request.evidences if e.status == EvidenceStatus.CONFIRMED]
        rejected = [e for e in request.evidences if e.status == EvidenceStatus.REJECTED]
        scores = [e.score for e in confirmed if e.score is not None]
        avg = sum(scores) / len(scores) if scores else 0.0
        bullish = sum("bull" in (e.reason or "").lower() for e in confirmed)
        bearish = sum("bear" in (e.reason or "").lower() for e in confirmed)
        decision = DecisionDirection.WAIT
        if confirmed and bullish > bearish:
            decision = DecisionDirection.BUY
        elif confirmed and bearish > bullish:
            decision = DecisionDirection.SELL
        confidence = max(0.0, min(1.0, avg))
        return DecisionResult(
            symbol=request.symbol,
            timeframe=request.timeframe,
            decision=decision,
            confidence=confidence,
            quality_score=round(confidence * 100, 2),
            risk_score=request.risk_score,
            confirmations=confirmed,
            rejected=rejected,
            source_count=len(request.evidences),
        )
