from app.platform_core.ai_decision.consensus import ai_consensus_engine
from app.platform_core.ai_decision.health import ai_decision_health_service
from app.platform_core.ai_decision.pipeline import ai_decision_pipeline
from app.platform_core.ai_decision.quality_gate import ai_decision_quality_gate
from app.platform_core.ai_decision.ranking import ai_signal_ranking_service
from app.platform_core.ai_decision.runtime_acceptance import ai_decision_runtime_acceptance_contract
from app.platform_core.ai_decision.service import ai_decision_core_service

class AIDecisionServicesPackageB:
    def context(self): return ai_decision_core_service.sample_context()
    def evidence(self): return ai_decision_core_service.sample_evidence()
    def consensus(self): return ai_consensus_engine.consensus(self.evidence())
    def ranking(self): return ai_signal_ranking_service.rank(self.evidence())
    def pipeline(self): return ai_decision_pipeline.run(self.context(), self.evidence())
    def quality_gate(self): return ai_decision_quality_gate.evaluate(self.pipeline())
    def health(self): return ai_decision_health_service.health()
    def runtime_acceptance(self): return ai_decision_runtime_acceptance_contract.contract()
    def status(self):
        pipeline = self.pipeline()
        gate = self.quality_gate()
        return {"ready": pipeline["ready"] and gate["ready"], "quality_passed": gate["passed"], "execution_allowed": False}

ai_decision_services_package_b = AIDecisionServicesPackageB()
