class AIConfidenceEngine:
    def calculate(self, evidence: list[dict]):
        if not evidence:
            return {"ready": True, "confidence": 0.0, "reason": "no_evidence"}
        total_weight = sum(float(x.get("weight", 1.0)) for x in evidence)
        if total_weight <= 0:
            return {"ready": False, "confidence": 0.0, "reason": "invalid_weight"}
        weighted_score = sum(float(x.get("score", 0.0)) * float(x.get("weight", 1.0)) for x in evidence)
        confidence = max(0.0, min(100.0, weighted_score / total_weight))
        return {"ready": True, "confidence": confidence, "reason": "weighted_evidence_score"}
ai_confidence_engine = AIConfidenceEngine()
