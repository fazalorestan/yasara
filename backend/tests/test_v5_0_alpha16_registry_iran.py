from app.platform_core.exchanges.registry import ExchangeRegistry
def test_v500_alpha16_registry_iran():
    r = ExchangeRegistry().seed_defaults()
    assert r["nobitex"]["region"] == "iran"
    assert r["wallex"]["region"] == "iran"
