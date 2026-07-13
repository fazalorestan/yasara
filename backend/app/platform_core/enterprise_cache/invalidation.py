from app.platform_core.enterprise_cache.memory import enterprise_memory_cache

class CacheInvalidationService:
    def invalidate(self, key: str):
        removed = enterprise_memory_cache.invalidate(key)
        return {"ready": True, "key": key, "removed": removed is not None}

    def clear_all(self):
        count = enterprise_memory_cache.clear()
        return {"ready": True, "cleared": count}

cache_invalidation_service = CacheInvalidationService()
