from app.platform_core.ai_decision.services_package_b import ai_decision_services_package_b

class AIDecisionServicesReadinessGate:
    def run(self):
        pipeline = ai_decision_services_package_b.pipeline()
        quality = ai_decision_services_package_b.quality_gate()
        health = ai_decision_services_package_b.health()
        runtime = ai_decision_services_package_b.runtime_acceptance()
        ready = pipeline["ready"] and quality["ready"] and health["ready"] and runtime["ready"]
        return {
            "ready": ready,
            "checks": {
                "pipeline_ready": pipeline["ready"],
                "quality_gate_ready": quality["ready"],
                "health_ready": health["ready"],
                "runtime_acceptance_ready": runtime["ready"],
                "real_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

ai_decision_services_readiness_gate = AIDecisionServicesReadinessGate()
