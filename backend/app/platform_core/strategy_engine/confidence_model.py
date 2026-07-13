class StrategyConfidenceModel:
    def confidence(self, score: float = 0.0):
        value = max(0.0, min(1.0, abs(float(score))))
        return {"ready": True, "confidence": value, "confidence_band": "low" if value < 0.4 else "medium" if value < 0.7 else "high"}

strategy_confidence_model = StrategyConfidenceModel()
