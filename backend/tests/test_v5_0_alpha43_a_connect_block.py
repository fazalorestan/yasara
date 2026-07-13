from app.platform_core.broker_layer.broker_safety import BrokerSafetyPolicy

def test_v500_alpha43_a_connect_block(): assert BrokerSafetyPolicy().can_connect_real_broker()['allowed'] is False
