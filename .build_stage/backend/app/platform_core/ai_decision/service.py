from app.platform_core.ai_decision.confidence import ai_confidence_engine
from app.platform_core.ai_decision.events import ai_decision_event_builder
from app.platform_core.ai_decision.explainability import ai_explainability_engine
from app.platform_core.ai_decision.metrics import ai_decision_metrics_service
from app.platform_core.ai_decision.safety import ai_decision_safety_contract

class AIDecisionCoreService:
    def sample_context(self):
        return {"symbol": "BTCUSDT", "timeframe": "1h", "signal_source": "scanner", "market_regime": "trend", "risk_state": "normal"}

    def sample_evidence(self):
        return [
            {"source": "scanner", "direction": "long", "score": 82.0, "reason": "high_rank", "weight": 1.0},
            {"source": "optimizer", "direction": "long", "score": 76.0, "reason": "robust_trial", "weight": 1.2},
            {"source": "risk", "direction": "neutral", "score": 65.0, "reason": "risk_normal", "weight": 0.8},
        ]

    def confidence(self): return ai_confidence_engine.calculate(self.sample_evidence())
    def explanation(self): return ai_explainability_engine.explain(self.sample_context(), self.sample_evidence(), self.confidence()["confidence"])
    def trace(self):
        return {"ready": True, "decision_id": "ai_decision_demo", "context": self.sample_context(), "evidence": self.sample_evidence(), "confidence": self.confidence()["confidence"], "explanation": self.explanation()["explanation"], "execution_allowed": False}
    def metrics(self): return ai_decision_metrics_service.summarize([self.trace()])
    def event(self): return ai_decision_event_builder.build("ai_decision_created", self.trace(), "info")
    def safety(self): return ai_decision_safety_contract.policy()
ai_decision_core_service = AIDecisionCoreService()
