from app.platform_core.production_runtime.service_report import runtime_service_report_service

class RuntimeServiceReadinessGate:
    def run(self):
        report = runtime_service_report_service.report()
        ready = (
            report["ready"]
            and report["registry"]["count"] >= 5
            and report["dependency_graph"]["acyclic"]
            and report["health"]["services_healthy"]
            and report["orchestration"]["orchestrated"]
            and report["commercial_execution_engine_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "registry_ready": report["registry"]["ready"],
                "dependency_graph_acyclic": report["dependency_graph"]["acyclic"],
                "services_healthy": report["health"]["services_healthy"],
                "orchestrated": report["orchestration"]["orchestrated"],
                "commercial_execution_engine_enabled": False,
                "commercial_api_key_required": False,
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

runtime_service_readiness_gate = RuntimeServiceReadinessGate()
