from app.platform_core.enterprise_queue.metrics import QueueMetricsReporter

def test_v437_metrics():
    r = QueueMetricsReporter().report()
    assert r["ready"] is True
    assert r["mode"] == "report_only"
