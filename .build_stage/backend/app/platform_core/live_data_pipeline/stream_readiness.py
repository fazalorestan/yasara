from app.platform_core.live_data_pipeline.stream_report import live_stream_manager_report
class LiveStreamManagerReadinessGate:
    def run(self):
        report = live_stream_manager_report.report()
        ready = report["ready"] and report["heartbeat"]["alive"] and report["execution_allowed"] is False
        return {"ready": ready, "checks": {"report_ready": report["ready"], "heartbeat_alive": report["heartbeat"]["alive"], "real_connection_allowed": False, "real_websocket_allowed": False, "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}
live_stream_manager_readiness_gate = LiveStreamManagerReadinessGate()
