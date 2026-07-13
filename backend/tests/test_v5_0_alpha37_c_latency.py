from app.platform_core.broker_layer.latency import BrokerLatencyMonitor

def test_v500_alpha37_c_latency(): assert BrokerLatencyMonitor().ping()['latency_ms']==0