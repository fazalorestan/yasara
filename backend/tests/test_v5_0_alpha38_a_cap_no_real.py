from app.platform_core.exchange_layer.capabilities import ExchangeCapabilityService

def test_v500_alpha38_a_cap_no_real(): assert ExchangeCapabilityService().detect({'exchange_id':'x'})['real_connection'] is False