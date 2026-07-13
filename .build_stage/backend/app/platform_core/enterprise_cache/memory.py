from app.platform_core.enterprise_cache.models import CacheEntry

class EnterpriseMemoryCache:
    def __init__(self):
        self._items: dict[str, CacheEntry] = {}

    def set(self, key: str, value, ttl_seconds: int = 300):
        entry = CacheEntry(key=key, value=value, ttl_seconds=ttl_seconds)
        self._items[key] = entry
        return entry

    def get(self, key: str, default=None):
        entry = self._items.get(key)
        if not entry:
            return default
        entry.hits += 1
        return entry.value

    def invalidate(self, key: str):
        return self._items.pop(key, None)

    def clear(self):
        count = len(self._items)
        self._items.clear()
        return count

    def snapshot(self):
        return {k: {**v.__dict__, "value": str(v.value)} for k, v in self._items.items()}

enterprise_memory_cache = EnterpriseMemoryCache()
