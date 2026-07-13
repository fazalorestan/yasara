from app.platform_core.enterprise_cache.metrics import CacheMetricsReporter

def test_v438_metrics():
    r = CacheMetricsReporter().report()
    assert r["ready"] is True
