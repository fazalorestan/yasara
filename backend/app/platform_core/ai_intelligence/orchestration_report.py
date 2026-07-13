from app.platform_core.ai_intelligence.prompt_orchestrator import ai_prompt_orchestrator
from app.platform_core.ai_intelligence.prompt_registry import ai_prompt_registry
from app.platform_core.ai_intelligence.tool_contract import ai_tool_contract_service
from app.platform_core.ai_intelligence.tool_registry import ai_tool_registry
from app.platform_core.ai_intelligence.tool_safety import ai_tool_safety_policy

class AIOrchestrationReport:
    def report(self):
        return {
            "ready": True,
            "prompts": ai_prompt_registry.list_prompts(),
            "orchestration": ai_prompt_orchestrator.orchestrate(),
            "tools": ai_tool_registry.list_tools(),
            "tool_contract": ai_tool_contract_service.contract(),
            "tool_dry_run": ai_tool_contract_service.dry_run(),
            "tool_safety": ai_tool_safety_policy.policy(),
            "real_provider_connection": False,
            "tool_execution_allowed": False,
            "execution_allowed": False,
        }

ai_orchestration_report = AIOrchestrationReport()
