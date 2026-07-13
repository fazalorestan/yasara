from app.platform_core.broker_layer.heartbeat import BrokerHeartbeatMonitor

def test_v500_alpha37_c_heartbeat(): assert BrokerHeartbeatMonitor().heartbeat()['alive'] is True