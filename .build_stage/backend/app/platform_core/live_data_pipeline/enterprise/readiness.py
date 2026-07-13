from app.platform_core.live_data_pipeline.enterprise.service import live_data_enterprise_service

class LiveDataEnterpriseReadinessGate:
    def run(self):
        security = live_data_enterprise_service.security()
        performance = live_data_enterprise_service.performance()
        quality = live_data_enterprise_service.quality_score()
        runtime = live_data_enterprise_service.runtime_acceptance()
        status = live_data_enterprise_service.final_status()
        ready = security["ready"] and performance["ready"] and quality["ready"] and runtime["ready"] and status["ready"]
        return {
            "ready": ready,
            "checks": {
                "security_ready": security["ready"],
                "performance_ready": performance["ready"],
                "quality_ready": quality["ready"],
                "runtime_ready": runtime["ready"],
                "final_status_ready": status["ready"],
                "real_connection_allowed": False,
                "real_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

live_data_enterprise_readiness_gate = LiveDataEnterpriseReadinessGate()
