from app.platform_core.ai_intelligence.context_contract import ai_context_contract_service
from app.platform_core.ai_intelligence.kernel import ai_kernel_service
from app.platform_core.ai_intelligence.prompt_contract import ai_prompt_contract_service
from app.platform_core.ai_intelligence.provider_contract import ai_provider_contract_service
from app.platform_core.ai_intelligence.provider_registry import ai_provider_registry
from app.platform_core.ai_intelligence.safety import ai_safety_policy

class AICoreKernelReport:
    def report(self):
        prompt = ai_prompt_contract_service.prompt()
        context = ai_context_contract_service.context()
        return {
            "ready": True,
            "kernel": ai_kernel_service.kernel_status(),
            "providers": ai_provider_registry.list_providers(),
            "provider_contract": ai_provider_contract_service.contract(),
            "prompt": prompt,
            "prompt_validation": ai_prompt_contract_service.validate(prompt),
            "context": context,
            "context_validation": ai_context_contract_service.validate(context),
            "safety": ai_safety_policy.policy(),
            "real_provider_connection": False,
            "execution_allowed": False,
        }

ai_core_kernel_report = AICoreKernelReport()
