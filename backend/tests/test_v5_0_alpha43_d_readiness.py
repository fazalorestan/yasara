from app.platform_core.broker_layer.monitoring_readiness import BrokerMonitoringReadinessGate

def test_v500_alpha43_d_readiness(): assert BrokerMonitoringReadinessGate().run()['ready'] is True
