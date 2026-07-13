class AIProviderContractService:
    def contract(self):
        return {
            "ready": True,
            "interface": "ai_provider_contract",
            "methods": ["metadata", "complete", "embed", "health"],
            "real_provider_connection": False,
            "api_key_required": False,
            "execution_allowed": False,
        }

    def simulated_completion(self, prompt: str = "ping"):
        return {
            "ready": True,
            "prompt": prompt,
            "response": "simulated_ai_response",
            "provider": "sim.local",
            "real_provider_connection": False,
            "execution_allowed": False,
        }

ai_provider_contract_service = AIProviderContractService()
