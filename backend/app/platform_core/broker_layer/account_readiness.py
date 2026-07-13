from app.platform_core.broker_layer.account_report import broker_account_report
class BrokerAccountReadinessGate:
    def run(self):
        report = broker_account_report.report()
        ready = report["ready"] and report["safety"]["real_account_read_enabled"] is False and report["execution_allowed"] is False
        return {"ready": ready, "checks": {"report_ready": report["ready"], "real_account_read_allowed": False, "real_broker_connection_allowed": False, "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}
broker_account_readiness_gate = BrokerAccountReadinessGate()
