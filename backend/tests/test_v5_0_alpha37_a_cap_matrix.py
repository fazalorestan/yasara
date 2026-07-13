from app.platform_core.broker_layer.capabilities import BrokerCapabilityService

def test_v500_alpha37_a_cap_matrix(): assert BrokerCapabilityService().matrix([{'broker_id':'b'}])['ready'] is True