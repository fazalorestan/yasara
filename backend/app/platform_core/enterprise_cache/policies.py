from app.platform_core.enterprise_cache.models import CachePolicy

class CachePolicyRegistry:
    def __init__(self):
        self._policies: dict[str, CachePolicy] = {}

    def register(self, policy: CachePolicy):
        self._policies[policy.name] = policy
        return policy

    def get(self, name: str):
        return self._policies.get(name)

    def list(self):
        return {k: v.__dict__ for k, v in self._policies.items()}

    def seed_defaults(self):
        if not self._policies:
            self.register(CachePolicy(name="market_data", ttl_seconds=15))
            self.register(CachePolicy(name="diagnostics", ttl_seconds=300))
            self.register(CachePolicy(name="plugin_catalog", ttl_seconds=600))
        return self.list()

cache_policy_registry = CachePolicyRegistry()
