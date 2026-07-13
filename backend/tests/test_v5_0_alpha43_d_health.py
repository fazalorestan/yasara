from app.platform_core.broker_layer.broker_health_monitor import BrokerHealthMonitorService

def test_v500_alpha43_d_health(): assert BrokerHealthMonitorService().health()['status']=='dry_healthy'
