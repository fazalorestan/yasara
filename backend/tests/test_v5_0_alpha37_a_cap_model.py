from app.platform_core.broker_layer.models import BrokerCapability

def test_v500_alpha37_a_cap_model(): assert BrokerCapability('b').supports_balances is False