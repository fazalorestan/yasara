class AIExplainabilityEngine:
    def explain(self, context: dict, evidence: list[dict], confidence: float):
        votes = {}
        for item in evidence:
            direction = item.get("direction", "neutral")
            votes[direction] = votes.get(direction, 0) + 1
        dominant = max(votes, key=votes.get) if votes else "neutral"
        symbol = context.get("symbol", "UNKNOWN")
        return {"ready": True, "symbol": symbol, "dominant_direction": dominant, "confidence": confidence, "explanation": f"AI decision for {symbol}: dominant direction is {dominant} with confidence {confidence:.2f}."}
ai_explainability_engine = AIExplainabilityEngine()
