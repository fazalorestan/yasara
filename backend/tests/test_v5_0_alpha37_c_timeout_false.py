from app.platform_core.broker_layer.heartbeat import BrokerHeartbeatMonitor

def test_v500_alpha37_c_timeout_false(): assert BrokerHeartbeatMonitor().timeout_check(0)['timed_out'] is False