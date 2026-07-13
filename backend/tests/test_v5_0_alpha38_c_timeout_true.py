from app.platform_core.exchange_layer.heartbeat import ExchangeHeartbeatMonitor

def test_v500_alpha38_c_timeout_true(): assert ExchangeHeartbeatMonitor().timeout_check(40000)['timed_out'] is True