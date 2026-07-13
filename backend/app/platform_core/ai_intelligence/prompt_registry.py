class AIPromptRegistry:
    def __init__(self):
        self._prompts = {
            "analysis.default": {"prompt_id": "analysis.default", "version": "v1", "task": "analysis", "enabled": True},
            "risk.default": {"prompt_id": "risk.default", "version": "v1", "task": "risk", "enabled": True},
        }

    def list_prompts(self):
        return {"ready": True, "prompts": list(self._prompts.values()), "count": len(self._prompts)}

    def get(self, prompt_id: str):
        prompt = self._prompts.get(prompt_id)
        return {"ready": prompt is not None, "prompt": prompt}

ai_prompt_registry = AIPromptRegistry()
