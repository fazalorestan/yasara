from app.platform_core.build_pipeline.report import build_pipeline_report_service

class PipelineStatusProvider:
    def status(self):
        report = build_pipeline_report_service.report()
        return {
            "ready": True,
            "pipeline_ready": report["ready"],
            "build_enabled": report["core"]["build_enabled"],
            "packaging_enabled": report["packaging_enabled"],
            "validation": report["validation"]["build_valid"],
            "integrity": report["integrity"]["integrity_valid"],
            "source": "build_pipeline_report",
            "hardcoded_dashboard": False,
        }

pipeline_status_provider = PipelineStatusProvider()
