from app.platform_core.execution_engine.analytics_report import execution_analytics_report

class ExecutionAnalyticsReadinessGate:
    def run(self):
        report = execution_analytics_report.report()
        ready = report["ready"] and report["compliance_log"]["passed"] and report["execution_allowed"] is False
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "compliance_passed": report["compliance_log"]["passed"],
                "analytics_only": report["safety"]["analytics_only"],
                "real_execution_allowed": False,
                "broker_connection_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

execution_analytics_readiness_gate = ExecutionAnalyticsReadinessGate()
