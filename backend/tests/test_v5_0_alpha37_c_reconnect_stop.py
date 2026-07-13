from app.platform_core.broker_layer.reconnect import BrokerReconnectPolicy

def test_v500_alpha37_c_reconnect_stop(): assert BrokerReconnectPolicy().attempt(3)['retry_allowed'] is False