from app.platform_core.broker_layer.broker_report import broker_core_report

class BrokerCoreReadinessGate:
    def run(self):
        report = broker_core_report.report()
        ready = report["ready"] and report["safety"]["real_broker_connection_enabled"] is False and report["execution_allowed"] is False
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "real_broker_connection_allowed": False,
                "real_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

broker_core_readiness_gate = BrokerCoreReadinessGate()
