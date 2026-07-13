from app.platform_core.broker_layer.heartbeat import BrokerHeartbeatMonitor

def test_v500_alpha37_c_timeout_true(): assert BrokerHeartbeatMonitor().timeout_check(40000)['timed_out'] is True