from app.platform_core.risk_engine.exposure import exposure_guard
class AIDecisionRiskLink:
    def check(self, exposure_pct: float = 50.0):
        result = exposure_guard.check_portfolio_exposure(exposure_pct, 60.0)
        return {"ready": result["ready"], "allowed": result["allowed"], "reason": result["reason"], "source": "risk_engine", "execution_allowed": False}
    def evidence(self):
        result = self.check()
        score = 75.0 if result["allowed"] else 25.0
        return {"ready": True, "evidence": [{"source": "risk_engine", "direction": "neutral", "score": score, "reason": result["reason"], "weight": 0.8}], "execution_allowed": False}
ai_decision_risk_link = AIDecisionRiskLink()
