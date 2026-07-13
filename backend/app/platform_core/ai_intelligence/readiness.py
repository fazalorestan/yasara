from app.platform_core.ai_intelligence.report import ai_core_kernel_report

class AICoreKernelReadinessGate:
    def run(self):
        report = ai_core_kernel_report.report()
        ready = (
            report["ready"]
            and report["prompt_validation"]["valid"]
            and report["context_validation"]["valid"]
            and report["execution_allowed"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "prompt_valid": report["prompt_validation"]["valid"],
                "context_valid": report["context_validation"]["valid"],
                "real_provider_connection_allowed": False,
                "tool_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

ai_core_kernel_readiness_gate = AICoreKernelReadinessGate()
