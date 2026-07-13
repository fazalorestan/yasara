from app.platform_core.exchange_layer.heartbeat import ExchangeHeartbeatMonitor

def test_v500_alpha38_c_heartbeat(): assert ExchangeHeartbeatMonitor().heartbeat()['alive'] is True