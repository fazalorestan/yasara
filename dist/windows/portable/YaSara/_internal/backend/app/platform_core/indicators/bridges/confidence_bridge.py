class IndicatorConfidenceBridge:
    def normalize(self, value):
        try:
            score = int(value)
        except Exception:
            score = 0
        return max(0, min(score, 100))

    def grade(self, value):
        score = self.normalize(value)
        if score >= 85:
            return "A+"
        if score >= 75:
            return "A"
        if score >= 65:
            return "B+"
        if score >= 55:
            return "B"
        if score >= 45:
            return "C"
        return "D"

indicator_confidence_bridge = IndicatorConfidenceBridge()
