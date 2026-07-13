from app.platform_core.ai_intelligence.agent_runtime_report import ai_agent_runtime_report
from app.platform_core.ai_intelligence.enterprise.performance import ai_enterprise_performance_gate
from app.platform_core.ai_intelligence.enterprise.quality_score import ai_enterprise_quality_score_service
from app.platform_core.ai_intelligence.enterprise.report import ai_enterprise_report_builder
from app.platform_core.ai_intelligence.enterprise.runtime_acceptance import ai_enterprise_runtime_acceptance
from app.platform_core.ai_intelligence.enterprise.security import ai_enterprise_security_gate
from app.platform_core.ai_intelligence.memory_report import ai_memory_context_report
from app.platform_core.ai_intelligence.orchestration_report import ai_orchestration_report
from app.platform_core.ai_intelligence.report import ai_core_kernel_report

class AIEnterpriseService:
    def security(self): return ai_enterprise_security_gate.evaluate()
    def performance(self): return ai_enterprise_performance_gate.evaluate()
    def quality_score(self):
        return ai_enterprise_quality_score_service.calculate(
            security=self.security()["score"],
            performance=self.performance()["score"],
        )
    def runtime_acceptance(self): return ai_enterprise_runtime_acceptance.contract()
    def final_report(self): return ai_enterprise_report_builder.build()
    def final_status(self):
        core = ai_core_kernel_report.report()
        memory = ai_memory_context_report.report()
        orchestration = ai_orchestration_report.report()
        runtime = ai_agent_runtime_report.report()
        quality = self.quality_score()
        return {
            "ready": core["ready"] and memory["ready"] and orchestration["ready"] and runtime["ready"] and quality["ready"],
            "core_ready": core["ready"],
            "memory_ready": memory["ready"],
            "orchestration_ready": orchestration["ready"],
            "agent_runtime_ready": runtime["ready"],
            "quality_ready": quality["ready"],
            "quality_score": quality["overall"],
            "execution_allowed": False,
        }

ai_enterprise_service = AIEnterpriseService()
