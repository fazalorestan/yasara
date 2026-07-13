from app.platform_core.exchange_layer.capabilities import ExchangeCapabilityService

def test_v500_alpha38_a_cap_matrix(): assert ExchangeCapabilityService().matrix([{'exchange_id':'b'}])['ready'] is True