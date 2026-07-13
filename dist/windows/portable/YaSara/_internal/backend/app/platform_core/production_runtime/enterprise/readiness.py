from app.platform_core.production_runtime.enterprise.report import runtime_enterprise_report_service

class RuntimeEnterpriseReadinessGate:
    def run(self):
        report = runtime_enterprise_report_service.report()
        ready = (
            report["ready"]
            and report["security"]["ready"]
            and report["performance"]["ready"]
            and report["quality"]["ready"]
            and report["acceptance"]["ready"]
            and report["commercial_execution_engine_enabled"] is False
            and report["commercial_api_key_required"] is False
            and report["real_execution_enabled"] is False
            and report["real_broker_connection_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "enterprise_report_ready": report["ready"],
                "security_ready": report["security"]["ready"],
                "performance_ready": report["performance"]["ready"],
                "quality_ready": report["quality"]["ready"],
                "acceptance_ready": report["acceptance"]["ready"],
                "commercial_execution_engine_enabled": False,
                "commercial_api_key_required": False,
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

runtime_enterprise_readiness_gate = RuntimeEnterpriseReadinessGate()
