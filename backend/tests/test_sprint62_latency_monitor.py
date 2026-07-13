from app.connectivity_v1.latency import LatencyMonitorV1, LatencySampleV1

def test_latency_monitor_level_low():
    report = LatencyMonitorV1().report("bitunix", [LatencySampleV1(exchange="bitunix", latency_ms=100)])
    assert report.level == "low"
    assert report.average_ms == 100
