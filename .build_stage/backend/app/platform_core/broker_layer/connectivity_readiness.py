from app.platform_core.broker_layer.connectivity_report import broker_connectivity_report_service
class BrokerConnectivityReadinessGate:
    def run(self):
        report = broker_connectivity_report_service.report()
        ready = report["ready"] and report["availability"]["available"] and report["execution_allowed"] is False
        return {"ready": ready, "checks": {"report_ready": report["ready"], "availability_ready": report["availability"]["ready"], "available": report["availability"]["available"], "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}
broker_connectivity_readiness_gate = BrokerConnectivityReadinessGate()
