from app.platform_core.enterprise_storage.metrics import StorageMetricsReporter

def test_v439_metrics():
    r = StorageMetricsReporter().report()
    assert r["ready"] is True
