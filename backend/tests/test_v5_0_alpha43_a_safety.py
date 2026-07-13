from app.platform_core.broker_layer.broker_safety import BrokerSafetyPolicy

def test_v500_alpha43_a_safety(): assert BrokerSafetyPolicy().policy()['real_broker_connection_enabled'] is False
