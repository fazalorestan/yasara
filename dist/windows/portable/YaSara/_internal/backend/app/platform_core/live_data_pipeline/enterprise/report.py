from app.platform_core.live_data_pipeline.cache_report import live_data_cache_report_service
from app.platform_core.live_data_pipeline.report import live_data_pipeline_core_report
from app.platform_core.live_data_pipeline.stream_report import live_stream_manager_report

class LiveDataEnterpriseReportBuilder:
    def build(self):
        return {
            "ready": True,
            "sprint": "v5.0-alpha.39",
            "name": "Live Data Pipeline",
            "packages": [
                "A-Data-Source-Ingestion",
                "B-Validation-Layer-Reserved",
                "C-Live-Stream-Manager",
                "D-Snapshot-Cache-History",
                "E-Enterprise",
            ],
            "core_report": live_data_pipeline_core_report.report(),
            "stream_report": live_stream_manager_report.report(),
            "cache_report": live_data_cache_report_service.report(),
            "real_connection": False,
            "real_websocket": False,
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

live_data_enterprise_report_builder = LiveDataEnterpriseReportBuilder()
