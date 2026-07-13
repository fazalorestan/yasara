from app.platform_core.build_pipeline.report import build_pipeline_report_service

class BuildPipelineReadinessGate:
    def run(self):
        report = build_pipeline_report_service.report()
        ready = (
            report["ready"]
            and report["core"]["build_enabled"]
            and report["manifest"]["backward_compatible"]
            and report["validation"]["build_valid"]
            and report["integrity"]["integrity_valid"]
            and report["plugin_contract"]["plugin_based_required"]
            and report["hardcoded_dashboard"] is False
            and report["commercial_execution_engine_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "core_ready": report["core"]["ready"],
                "manifest_ready": report["manifest"]["ready"],
                "metadata_ready": report["metadata"]["ready"],
                "validation_ready": report["validation"]["build_valid"],
                "integrity_ready": report["integrity"]["integrity_valid"],
                "plugin_based_required": report["plugin_contract"]["plugin_based_required"],
                "dashboard_ready": report["dashboard"]["ready"],
                "packaging_enabled": report["packaging_enabled"],
                "hardcoded_dashboard": False,
                "commercial_execution_engine_enabled": False,
                "commercial_api_key_required": False,
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

build_pipeline_readiness_gate = BuildPipelineReadinessGate()
