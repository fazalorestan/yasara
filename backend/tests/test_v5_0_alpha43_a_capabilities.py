from app.platform_core.broker_layer.broker_capability import BrokerCapabilityService

def test_v500_alpha43_a_capabilities(): assert BrokerCapabilityService().capabilities()['supports_real_orders'] is False
