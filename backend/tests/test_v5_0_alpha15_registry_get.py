from app.platform_core.market_data.registry import MarketDataRegistry
def test_v500_alpha15_registry_get():
    r = MarketDataRegistry()
    r.seed_defaults()
    assert r.get_symbol("ETHUSDT")["base_asset"] == "ETH"
