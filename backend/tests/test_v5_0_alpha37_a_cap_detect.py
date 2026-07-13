from app.platform_core.broker_layer.capabilities import BrokerCapabilityService

def test_v500_alpha37_a_cap_detect(): assert BrokerCapabilityService().detect({'broker_id':'b','mode':'paper'})['supports_balances'] is True