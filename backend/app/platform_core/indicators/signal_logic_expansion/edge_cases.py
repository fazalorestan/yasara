class SignalEdgeCaseResolver:
    def resolve_math_output(self, math_output: dict):
        if not math_output:
            return {"ready": False, "reason": "empty_math_output"}
        required_any = ["ema_21", "ema_55", "rsi_14", "macd", "atr_14"]
        if not any(math_output.get(k) is not None for k in required_any):
            return {"ready": False, "reason": "all_indicators_missing"}
        return {"ready": True, "reason": "math_output_usable"}

signal_edge_case_resolver = SignalEdgeCaseResolver()
