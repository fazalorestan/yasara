from app.platform_core.strategy_engine.scoring_report import strategy_scoring_report

class StrategyScoringReadinessGate:
    def run(self):
        report = strategy_scoring_report.report()
        ready = report["ready"] and report["rules"]["rules_passed"] and report["execution_allowed"] is False
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "rules_passed": report["rules"]["rules_passed"],
                "scoring_only": report["safety"]["scoring_only"],
                "real_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

strategy_scoring_readiness_gate = StrategyScoringReadinessGate()
