class YaSaraSignalAdapter:
    def normalize(self, raw: dict):
        direction = raw.get("direction", "WAIT")
        score = int(raw.get("score", 0))
        return {
            "indicator": "yasara",
            "direction": direction,
            "confidence": max(0, min(score, 100)),
            "risk": raw.get("risk", "safe"),
            "overlay_ready": True,
            "execution_allowed": False,
            "mode": "analysis_only",
        }

yasara_signal_adapter = YaSaraSignalAdapter()
