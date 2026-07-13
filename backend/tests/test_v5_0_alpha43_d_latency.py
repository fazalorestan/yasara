from app.platform_core.broker_layer.latency_monitor import BrokerLatencyMonitorService

def test_v500_alpha43_d_latency(): assert BrokerLatencyMonitorService().latency()['within_threshold'] is True
