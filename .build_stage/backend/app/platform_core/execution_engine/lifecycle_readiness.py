from app.platform_core.execution_engine.lifecycle_report import execution_lifecycle_report

class ExecutionLifecycleReadinessGate:
    def run(self):
        report = execution_lifecycle_report.report()
        ready = report["ready"] and report["journal"]["journaled"] and report["execution_allowed"] is False
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "journal_ready": report["journal"]["journaled"],
                "lifecycle_tracking_only": report["safety"]["lifecycle_tracking_only"],
                "real_execution_allowed": False,
                "broker_connection_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

execution_lifecycle_readiness_gate = ExecutionLifecycleReadinessGate()
