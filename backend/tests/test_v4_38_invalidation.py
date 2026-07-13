from app.platform_core.enterprise_cache.invalidation import CacheInvalidationService
from app.platform_core.enterprise_cache.memory import enterprise_memory_cache

def test_v438_invalidation():
    enterprise_memory_cache.set("x", "y")
    r = CacheInvalidationService().invalidate("x")
    assert r["removed"] is True
