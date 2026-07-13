from app.platform_core.enterprise_cache.invalidation import cache_invalidation_service
from app.platform_core.enterprise_cache.memory import enterprise_memory_cache
from app.platform_core.enterprise_cache.metrics import cache_metrics_reporter
from app.platform_core.enterprise_cache.policies import cache_policy_registry
from app.platform_core.enterprise_cache.redis_contract import redis_adapter_contract_service

class EnterpriseCacheService:
    def seed(self):
        return {"ready": True, "policies": cache_policy_registry.seed_defaults(), "mode": "report_only"}

    def set(self, key: str, value, ttl_seconds: int = 300):
        entry = enterprise_memory_cache.set(key, value, ttl_seconds)
        return {"ready": True, "entry": {**entry.__dict__, "value": str(entry.value)}}

    def get(self, key: str):
        return {"ready": True, "key": key, "value": enterprise_memory_cache.get(key)}

    def snapshot(self):
        return {"ready": True, "snapshot": enterprise_memory_cache.snapshot()}

    def metrics(self):
        return cache_metrics_reporter.report()

    def invalidate(self, key: str):
        return cache_invalidation_service.invalidate(key)

    def redis_contract(self):
        return {"ready": True, "redis": redis_adapter_contract_service.contract()}

enterprise_cache_service = EnterpriseCacheService()
