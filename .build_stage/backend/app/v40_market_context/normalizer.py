class ConfidenceNormalizerV40:
    def normalize(self, value):
        try:
            value = float(value)
        except Exception:
            return 0.0

        if value <= 0:
            return 0.0

        if value <= 1:
            value *= 100

        if value > 100:
            value = 100

        return round(value, 2)

    def weighted_score(self, results):
        if not results:
            return {"score": 50, "bias": "neutral"}

        total_weight = sum(max(r.weight, 0.01) for r in results)
        raw = 0

        for r in results:
            conf = self.normalize(r.confidence)
            direction = 1 if r.bias == "bullish" else -1 if r.bias == "bearish" else 0
            raw += (50 + direction * (conf - 50)) * r.weight

        score = round(raw / total_weight, 2)
        bias = "bullish" if score >= 60 else "bearish" if score <= 40 else "neutral"

        return {"score": score, "bias": bias}
