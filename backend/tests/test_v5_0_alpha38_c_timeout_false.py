from app.platform_core.exchange_layer.heartbeat import ExchangeHeartbeatMonitor

def test_v500_alpha38_c_timeout_false(): assert ExchangeHeartbeatMonitor().timeout_check(0)['timed_out'] is False