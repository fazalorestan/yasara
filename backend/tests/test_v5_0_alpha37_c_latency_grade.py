from app.platform_core.broker_layer.latency import BrokerLatencyMonitor

def test_v500_alpha37_c_latency_grade(): assert BrokerLatencyMonitor().latency_grade(0)['grade']=='excellent'