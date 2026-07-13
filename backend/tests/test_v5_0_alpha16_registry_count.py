from app.platform_core.exchanges.registry import ExchangeRegistry
def test_v500_alpha16_registry_count():
    r = ExchangeRegistry().seed_defaults()
    assert len(r) == 18
