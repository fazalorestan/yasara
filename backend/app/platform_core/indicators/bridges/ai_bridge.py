class IndicatorAIBridge:
    def to_ai_decision(self, runtime_output: dict):
        signals = runtime_output.get("signals", [])
        signal = signals[0] if signals else {}
        return {
            "ready": True,
            "source": "yasara_indicator",
            "direction": signal.get("direction", "WAIT"),
            "confidence": signal.get("confidence", 0),
            "reason": signal.get("reason", "no_signal"),
            "mode": "analysis_only",
        }

indicator_ai_bridge = IndicatorAIBridge()
