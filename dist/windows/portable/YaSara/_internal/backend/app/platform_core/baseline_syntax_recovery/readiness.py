from app.platform_core.baseline_syntax_recovery.report import (
    baseline_syntax_recovery_report_service,
)


class BaselineSyntaxRecoveryReadinessGate:
    def run(self):
        report = baseline_syntax_recovery_report_service.report()
        return {
            "ready": (
                report["ready"]
                and report["literal_newline_recovery"]
                and report["compile_validation_gate"]
                and report["auto_router_only"]
                and not report["auto_trading_enabled"]
            ),
            "checks": report,
        }


baseline_syntax_recovery_readiness_gate = BaselineSyntaxRecoveryReadinessGate()
