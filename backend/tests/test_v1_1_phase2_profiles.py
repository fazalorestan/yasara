from app.v11_exchange_connectivity.profiles import ExchangeProfileRegistryV11

def test_exchange_profiles():
    registry = ExchangeProfileRegistryV11()
    assert registry.get("binance").base_url.startswith("https://")
    assert set(registry.enabled_exchange_ids()) == {"binance", "bitunix", "toobit"}
