from app.platform_core.exchange_layer.capabilities import ExchangeCapabilityService

def test_v500_alpha38_a_cap_detect(): assert ExchangeCapabilityService().detect({'exchange_id':'binance.sandbox'})['futures'] is True