class SignalScoringEngineV42:
    def bias_to_score(self, bias, confidence=50):
        confidence = max(0, min(100, float(confidence)))
        if bias == "bullish":
            return confidence
        if bias == "bearish":
            return 100 - confidence
        return 50

    def risk_label(self, confidence, disagreement):
        if disagreement >= 3:
            return "high"
        if confidence >= 75 and disagreement <= 1:
            return "low"
        if confidence >= 60:
            return "medium"
        return "high"

    def action_from_score(self, score, risk):
        if risk == "high":
            return "wait"
        if score >= 64:
            return "long"
        if score <= 36:
            return "short"
        return "wait"

    def merge(self, layers):
        active = [x for x in layers if x.get("enabled", True)]
        if not active:
            return {"score": 50, "direction": "neutral", "confidence": 50, "risk": "high", "action": "wait"}

        total_weight = sum(max(float(x.get("weight", 1)), 0.01) for x in active)
        raw = 0
        bullish = bearish = neutral = 0
        reasons = []

        for item in active:
            bias = item.get("bias", "neutral")
            confidence = item.get("confidence", 50)
            weight = max(float(item.get("weight", 1)), 0.01)
            raw += self.bias_to_score(bias, confidence) * weight
            bullish += 1 if bias == "bullish" else 0
            bearish += 1 if bias == "bearish" else 0
            neutral += 1 if bias == "neutral" else 0
            reasons.extend(item.get("reasons", []))

        score = round(raw / total_weight, 2)
        direction = "bullish" if score >= 60 else "bearish" if score <= 40 else "neutral"
        confidence = round(abs(score - 50) * 2, 2)
        disagreement = min(bullish, bearish) + neutral
        risk = self.risk_label(confidence, disagreement)
        action = self.action_from_score(score, risk)

        return {
            "score": score,
            "direction": direction,
            "confidence": confidence,
            "risk": risk,
            "action": action,
            "votes": {"bullish": bullish, "bearish": bearish, "neutral": neutral},
            "reasons": reasons[:20],
        }
