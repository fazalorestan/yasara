from app.platform_core.live_data_pipeline.cache_report import live_data_cache_report_service

class LiveDataCacheReadinessGate:
    def run(self):
        report = live_data_cache_report_service.report()
        ready = report["ready"] and report["put"]["cached"] and report["execution_allowed"] is False
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "cache_write_ready": report["put"]["cached"],
                "cache_read_ready": report["get"]["ready"],
                "real_connection_allowed": False,
                "real_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

live_data_cache_readiness_gate = LiveDataCacheReadinessGate()
