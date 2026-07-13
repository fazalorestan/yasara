from app.platform_core.broker_layer.monitoring_report import broker_monitoring_report

class BrokerMonitoringReadinessGate:
    def run(self):
        report = broker_monitoring_report.report()
        ready = (
            report["ready"]
            and report["diagnostics"]["passed"]
            and report["latency"]["within_threshold"]
            and report["execution_allowed"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "diagnostics_passed": report["diagnostics"]["passed"],
                "latency_within_threshold": report["latency"]["within_threshold"],
                "monitoring_only": report["safety"]["monitoring_only"],
                "real_broker_connection_allowed": False,
                "real_account_read_allowed": False,
                "real_order_submit_allowed": False,
                "real_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

broker_monitoring_readiness_gate = BrokerMonitoringReadinessGate()
