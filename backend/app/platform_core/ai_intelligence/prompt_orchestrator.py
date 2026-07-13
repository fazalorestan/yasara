from app.platform_core.ai_intelligence.context_builder import ai_context_builder_service
from app.platform_core.ai_intelligence.prompt_contract import ai_prompt_contract_service
from app.platform_core.ai_intelligence.prompt_registry import ai_prompt_registry
from app.platform_core.ai_intelligence.prompt_versioning import ai_prompt_versioning_service

class AIPromptOrchestrator:
    def orchestrate(self, prompt_id: str = "analysis.default"):
        prompt = ai_prompt_registry.get(prompt_id)
        contract = ai_prompt_contract_service.prompt(prompt["prompt"]["task"] if prompt["ready"] else "analysis")
        context = ai_context_builder_service.build()
        version = ai_prompt_versioning_service.version(prompt_id)
        return {
            "ready": prompt["ready"] and contract["ready"] and context["ready"],
            "prompt": prompt,
            "contract": contract,
            "context": context,
            "version": version,
            "provider_invocation_allowed": False,
            "execution_allowed": False,
        }

ai_prompt_orchestrator = AIPromptOrchestrator()
