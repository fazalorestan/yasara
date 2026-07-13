from app.platform_core.enterprise_cache.service import enterprise_cache_service
from app.v438_enterprise_cache.models import EnterpriseCacheSummaryV438

class EnterpriseCacheFacadeV438:
    def summary(self):
        return EnterpriseCacheSummaryV438()

    def seed(self):
        return enterprise_cache_service.seed()

    def set(self, key: str = "diagnostics", value: str = "ready", ttl_seconds: int = 300):
        return enterprise_cache_service.set(key, value, ttl_seconds)

    def get(self, key: str = "diagnostics"):
        return enterprise_cache_service.get(key)

    def snapshot(self):
        return enterprise_cache_service.snapshot()

    def metrics(self):
        return enterprise_cache_service.metrics()

    def invalidate(self, key: str = "diagnostics"):
        return enterprise_cache_service.invalidate(key)

    def redis_contract(self):
        return enterprise_cache_service.redis_contract()
