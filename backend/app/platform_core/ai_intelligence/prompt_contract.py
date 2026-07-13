class AIPromptContractService:
    def prompt(self, task: str = "analyze"):
        return {
            "ready": True,
            "task": task,
            "system": "You are YaSara AI Kernel.",
            "user": "Simulated request",
            "version": "v1",
        }

    def validate(self, prompt: dict):
        required = ["system", "user", "task"]
        missing = [x for x in required if not prompt.get(x)]
        return {"ready": True, "valid": len(missing) == 0, "missing": missing}

ai_prompt_contract_service = AIPromptContractService()
