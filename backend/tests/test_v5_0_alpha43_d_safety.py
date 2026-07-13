from app.platform_core.broker_layer.monitoring_safety import BrokerMonitoringSafetyPolicy

def test_v500_alpha43_d_safety(): assert BrokerMonitoringSafetyPolicy().policy()['monitoring_only'] is True
