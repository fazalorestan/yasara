from app.platform_core.production_runtime.lifecycle_report import runtime_lifecycle_report_service

class RuntimeLifecycleReadinessGate:
    def run(self):
        report = runtime_lifecycle_report_service.report()
        ready = (
            report["ready"]
            and report["startup"]["completed"]
            and report["shutdown"]["completed"]
            and report["restart"]["completed"]
            and report["session"]["active"]
            and report["event_bus"]["publish_enabled"]
            and report["commercial_execution_engine_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "lifecycle_ready": report["lifecycle"]["ready"],
                "startup_completed": report["startup"]["completed"],
                "shutdown_completed": report["shutdown"]["completed"],
                "restart_completed": report["restart"]["completed"],
                "session_active": report["session"]["active"],
                "event_bus_ready": report["event_bus"]["ready"],
                "commercial_execution_engine_enabled": False,
                "commercial_api_key_required": False,
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

runtime_lifecycle_readiness_gate = RuntimeLifecycleReadinessGate()
