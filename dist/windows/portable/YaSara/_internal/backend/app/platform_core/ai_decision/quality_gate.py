class AIDecisionQualityGate:
    def evaluate(self, pipeline_result: dict):
        confidence = float(pipeline_result.get("decision", {}).get("confidence", 0.0))
        agreement = float(pipeline_result.get("consensus", {}).get("agreement_pct", 0.0))
        passed = pipeline_result.get("ready") is True and confidence >= 50.0 and agreement >= 50.0
        return {
            "ready": True,
            "passed": passed,
            "confidence": confidence,
            "agreement_pct": agreement,
            "min_confidence": 50.0,
            "min_agreement_pct": 50.0,
            "execution_allowed": False,
        }

ai_decision_quality_gate = AIDecisionQualityGate()
