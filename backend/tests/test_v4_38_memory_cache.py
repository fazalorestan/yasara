from app.platform_core.enterprise_cache.memory import EnterpriseMemoryCache

def test_v438_memory_cache():
    pass

    c = EnterpriseMemoryCache()
    c.set("a", 1)
    assert c.get("a") == 1
    assert c.snapshot()["a"]["hits"] == 1
