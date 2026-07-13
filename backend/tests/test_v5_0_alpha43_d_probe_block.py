from app.platform_core.broker_layer.monitoring_safety import BrokerMonitoringSafetyPolicy

def test_v500_alpha43_d_probe_block(): assert BrokerMonitoringSafetyPolicy().can_probe_real_broker()['allowed'] is False
