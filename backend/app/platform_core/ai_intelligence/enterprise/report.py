from app.platform_core.ai_intelligence.agent_runtime_report import ai_agent_runtime_report
from app.platform_core.ai_intelligence.memory_report import ai_memory_context_report
from app.platform_core.ai_intelligence.orchestration_report import ai_orchestration_report
from app.platform_core.ai_intelligence.report import ai_core_kernel_report

class AIEnterpriseReportBuilder:
    def build(self):
        return {
            "ready": True,
            "sprint": "v5.0-alpha.40",
            "name": "AI Intelligence Layer",
            "packages": [
                "A-AI-Core-Kernel",
                "B-Memory-Context",
                "C-Prompt-Tool-Orchestration",
                "D-Decision-Agent-Runtime",
                "E-Enterprise",
            ],
            "core_report": ai_core_kernel_report.report(),
            "memory_context_report": ai_memory_context_report.report(),
            "orchestration_report": ai_orchestration_report.report(),
            "agent_runtime_report": ai_agent_runtime_report.report(),
            "real_provider_connection": False,
            "agent_execution_enabled": False,
            "tool_execution_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

ai_enterprise_report_builder = AIEnterpriseReportBuilder()
