from app.platform_core.execution_engine.enterprise.service import execution_enterprise_service

class ExecutionEnterpriseReadinessGate:
    def run(self):
        security = execution_enterprise_service.security()
        performance = execution_enterprise_service.performance()
        quality = execution_enterprise_service.quality_score()
        runtime = execution_enterprise_service.runtime_acceptance()
        status = execution_enterprise_service.final_status()
        ready = security["ready"] and performance["ready"] and quality["ready"] and runtime["ready"] and status["ready"]
        return {
            "ready": ready,
            "checks": {
                "security_ready": security["ready"],
                "performance_ready": performance["ready"],
                "quality_ready": quality["ready"],
                "runtime_ready": runtime["ready"],
                "final_status_ready": status["ready"],
                "real_execution_allowed": False,
                "broker_connection_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

execution_enterprise_readiness_gate = ExecutionEnterpriseReadinessGate()
