from app.platform_core.exchange_layer.registry import ExchangeRegistryService

def test_v500_alpha38_a_registry_register(): assert ExchangeRegistryService().register({'exchange_id':'x'})['registered'] is True