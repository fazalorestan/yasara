from app.platform_core.optimizer_pro.service import strategy_optimizer_pro_service
class AIDecisionOptimizerLink:
    def best_trial(self):
        return {"ready": True, "best": strategy_optimizer_pro_service.best(), "source": "optimizer_pro", "execution_allowed": False}
    def evidence(self):
        best = self.best_trial()["best"]
        score = max(0.0, min(100.0, float(best.get("score", 0))))
        return {"ready": True, "evidence": [{"source": "optimizer_pro", "direction": "long", "score": score, "reason": "best_optimizer_trial", "weight": 1.2}], "execution_allowed": False}
ai_decision_optimizer_link = AIDecisionOptimizerLink()
