from app.platform_core.exchange_layer.latency import ExchangeLatencyMonitor

def test_v500_alpha38_c_latency_grade(): assert ExchangeLatencyMonitor().latency_grade(0)['grade']=='excellent'