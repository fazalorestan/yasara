from app.platform_core.strategy_engine.report import strategy_core_report

class StrategyCoreReadinessGate:
    def run(self):
        report = strategy_core_report.report()
        ready = report["ready"] and report["signal_validation"]["valid"] and report["rule_validation"]["valid"] and report["execution_allowed"] is False
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "signal_valid": report["signal_validation"]["valid"],
                "rules_valid": report["rule_validation"]["valid"],
                "real_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

strategy_core_readiness_gate = StrategyCoreReadinessGate()
