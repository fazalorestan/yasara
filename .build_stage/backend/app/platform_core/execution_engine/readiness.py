from app.platform_core.execution_engine.report import execution_core_report

class ExecutionCoreReadinessGate:
    def run(self):
        report = execution_core_report.report()
        ready = report["ready"] and report["intent_validation"]["valid"] and report["execution_allowed"] is False
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "intent_valid": report["intent_validation"]["valid"],
                "dry_run_only": report["safety"]["dry_run_only"],
                "real_execution_allowed": False,
                "broker_connection_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

execution_core_readiness_gate = ExecutionCoreReadinessGate()
