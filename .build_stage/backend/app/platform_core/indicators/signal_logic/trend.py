class TrendSignalLogic:
    def evaluate(self, math_output: dict):
        ema21 = math_output.get("ema_21")
        ema55 = math_output.get("ema_55")
        if ema21 is None or ema55 is None:
            return {"score": 0, "direction": "WAIT", "reason": "trend_insufficient_data"}
        if ema21 > ema55:
            return {"score": 30, "direction": "LONG", "reason": "ema21_above_ema55"}
        if ema21 < ema55:
            return {"score": 30, "direction": "SHORT", "reason": "ema21_below_ema55"}
        return {"score": 0, "direction": "WAIT", "reason": "trend_neutral"}

trend_signal_logic = TrendSignalLogic()
