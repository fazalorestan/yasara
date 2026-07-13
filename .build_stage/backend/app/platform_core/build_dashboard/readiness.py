from app.platform_core.build_dashboard.report import build_dashboard_integration_report_service

class BuildDashboardIntegrationReadinessGate:
    def run(self):
        report = build_dashboard_integration_report_service.report()
        ready = (
            report["ready"]
            and report["integration"]["ready"]
            and report["pipeline_status"]["ready"]
            and report["ci_signal"]["signal"] == "green"
            and report["release_signal"]["signal"] == "green"
            and report["artifact_signal"]["signal"] == "green"
            and report["quality_signal"]["signal"] == "green"
            and report["hardcoded_dashboard"] is False
            and report["commercial_execution_engine_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "integration_ready": report["integration"]["ready"],
                "pipeline_status_ready": report["pipeline_status"]["ready"],
                "ci_signal": report["ci_signal"]["signal"],
                "release_signal": report["release_signal"]["signal"],
                "artifact_signal": report["artifact_signal"]["signal"],
                "quality_signal": report["quality_signal"]["signal"],
                "packaging_enabled": report["packaging_enabled"],
                "hardcoded_dashboard": False,
                "commercial_execution_engine_enabled": False,
                "commercial_api_key_required": False,
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

build_dashboard_integration_readiness_gate = BuildDashboardIntegrationReadinessGate()
