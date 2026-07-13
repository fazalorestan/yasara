from app.platform_core.exchange_layer.latency import ExchangeLatencyMonitor

def test_v500_alpha38_c_latency(): assert ExchangeLatencyMonitor().ping()['latency_ms']==0