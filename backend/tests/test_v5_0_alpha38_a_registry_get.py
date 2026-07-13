from app.platform_core.exchange_layer.registry import ExchangeRegistryService

def test_v500_alpha38_a_registry_get(): assert ExchangeRegistryService().get('binance.sandbox')['ready'] is True