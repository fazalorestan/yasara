class MomentumSignalLogic:
    def evaluate(self, math_output: dict):
        rsi = math_output.get("rsi_14")
        macd = math_output.get("macd") or {}
        hist = macd.get("histogram")
        score = 0
        direction = "WAIT"
        reasons = []
        if rsi is not None:
            if rsi > 55:
                score += 15
                direction = "LONG"
                reasons.append("rsi_bullish")
            elif rsi < 45:
                score += 15
                direction = "SHORT"
                reasons.append("rsi_bearish")
        if hist is not None:
            if hist > 0:
                score += 15
                direction = "LONG" if direction in ["WAIT", "LONG"] else direction
                reasons.append("macd_hist_positive")
            elif hist < 0:
                score += 15
                direction = "SHORT" if direction in ["WAIT", "SHORT"] else direction
                reasons.append("macd_hist_negative")
        return {"score": score, "direction": direction, "reason": ",".join(reasons) or "momentum_neutral"}

momentum_signal_logic = MomentumSignalLogic()
