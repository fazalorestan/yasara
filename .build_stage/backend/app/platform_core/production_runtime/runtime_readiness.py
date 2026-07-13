from app.platform_core.production_runtime.runtime_safety import runtime_safety_policy
from app.platform_core.production_runtime.startup_report import runtime_startup_report_service

class RuntimeReadinessGate:
    def run(self):
        report = runtime_startup_report_service.report()
        safety = runtime_safety_policy.policy()
        ready = (
            report["ready"]
            and report["dry_boot"]["booted"]
            and report["commercial_mode"]["execution_engine_enabled"] is False
            and safety["real_execution_enabled"] is False
            and safety["real_broker_connection_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "startup_report_ready": report["ready"],
                "dry_boot_ready": report["dry_boot"]["booted"],
                "personal_execution_engine_enabled": report["personal_mode"]["execution_engine_enabled"],
                "commercial_execution_engine_enabled": report["commercial_mode"]["execution_engine_enabled"],
                "commercial_api_key_required": report["commercial_mode"]["api_key_required"],
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

runtime_readiness_gate = RuntimeReadinessGate()
