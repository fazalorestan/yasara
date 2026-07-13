from app.platform_core.exchange_layer.registry import ExchangeRegistryService

def test_v500_alpha38_a_registry_missing(): assert ExchangeRegistryService().get('missing')['ready'] is False