class VolatilitySignalLogic:
    def evaluate(self, math_output: dict):
        atr = math_output.get("atr_14")
        if atr is None:
            return {"score": 0, "risk": "unknown", "reason": "atr_insufficient_data"}
        if atr > 0:
            return {"score": 10, "risk": "active", "reason": "atr_available"}
        return {"score": 0, "risk": "flat", "reason": "atr_flat"}

volatility_signal_logic = VolatilitySignalLogic()
