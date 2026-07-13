from app.platform_core.live_data_pipeline.report import live_data_pipeline_core_report

class LiveDataPipelineCoreReadinessGate:
    def run(self):
        report = live_data_pipeline_core_report.report()
        ready = report["ready"] and report["validation"]["valid"] and report["execution_allowed"] is False
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "snapshot_valid": report["validation"]["valid"],
                "read_only": report["safety"]["read_only"],
                "real_live_connection_allowed": False,
                "real_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

live_data_pipeline_core_readiness_gate = LiveDataPipelineCoreReadinessGate()
