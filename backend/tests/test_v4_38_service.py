from app.platform_core.enterprise_cache.service import EnterpriseCacheService

def test_v438_service():
    s = EnterpriseCacheService()
    assert s.seed()["ready"] is True
    assert s.set("k", "v")["ready"] is True
    assert s.get("k")["value"] == "v"
