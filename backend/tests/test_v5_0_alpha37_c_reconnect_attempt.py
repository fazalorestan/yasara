from app.platform_core.broker_layer.reconnect import BrokerReconnectPolicy

def test_v500_alpha37_c_reconnect_attempt(): assert BrokerReconnectPolicy().attempt(0)['retry_allowed'] is True