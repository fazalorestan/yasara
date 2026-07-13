from app.platform_core.exchanges.registry import ExchangeRegistry
def test_v500_alpha16_registry_new_exchanges():
    r = ExchangeRegistry().seed_defaults()
    assert "bitunix" in r
    assert "toobit" in r
    assert "lbank" in r
