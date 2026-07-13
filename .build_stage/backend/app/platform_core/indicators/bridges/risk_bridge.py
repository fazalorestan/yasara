class IndicatorRiskBridge:
    def to_risk_panel(self, runtime_output: dict):
        signals = runtime_output.get("signals", [])
        signal = signals[0] if signals else {}
        confidence = int(signal.get("confidence", 0))
        risk_level = "low" if confidence >= 70 else "medium" if confidence >= 40 else "neutral"
        return {
            "ready": True,
            "source": "yasara_indicator",
            "risk_level": risk_level,
            "execution_allowed": False,
            "mode": "analysis_only",
        }

indicator_risk_bridge = IndicatorRiskBridge()
