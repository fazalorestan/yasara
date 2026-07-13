from app.platform_core.ai_intelligence.orchestration_report import ai_orchestration_report

class AIOrchestrationReadinessGate:
    def run(self):
        report = ai_orchestration_report.report()
        ready = report["ready"] and report["tool_safety"]["tool_execution_enabled"] is False
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "prompts_ready": report["prompts"]["ready"],
                "tools_ready": report["tools"]["ready"],
                "provider_invocation_allowed": False,
                "tool_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

ai_orchestration_readiness_gate = AIOrchestrationReadinessGate()
