class AIProviderRegistry:
    def __init__(self):
        self._providers = {
            "sim.local": {"provider_id": "sim.local", "name": "Simulated Local AI", "mode": "simulated", "enabled": True},
            "sim.cloud": {"provider_id": "sim.cloud", "name": "Simulated Cloud AI", "mode": "simulated", "enabled": True},
        }

    def list_providers(self):
        return {"ready": True, "providers": list(self._providers.values()), "count": len(self._providers)}

    def get(self, provider_id: str):
        provider = self._providers.get(provider_id)
        return {"ready": provider is not None, "provider": provider}

    def register(self, provider: dict):
        if not provider.get("provider_id"):
            return {"ready": False, "registered": False, "reason": "missing_provider_id"}
        self._providers[provider["provider_id"]] = provider
        return {"ready": True, "registered": True, "provider_id": provider["provider_id"]}

ai_provider_registry = AIProviderRegistry()
