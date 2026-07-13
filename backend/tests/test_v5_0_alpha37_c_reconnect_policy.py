from app.platform_core.broker_layer.reconnect import BrokerReconnectPolicy

def test_v500_alpha37_c_reconnect_policy(): assert BrokerReconnectPolicy().policy()['simulated_only'] is True