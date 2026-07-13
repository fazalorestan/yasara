from app.platform_core.ai_intelligence.agent_runtime_report import ai_agent_runtime_report

class AIAgentRuntimeReadinessGate:
    def run(self):
        report = ai_agent_runtime_report.report()
        ready = report["ready"] and report["graph_validation"]["valid"] and report["execution_allowed"] is False
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "graph_valid": report["graph_validation"]["valid"],
                "agent_execution_allowed": False,
                "real_provider_connection_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

ai_agent_runtime_readiness_gate = AIAgentRuntimeReadinessGate()
