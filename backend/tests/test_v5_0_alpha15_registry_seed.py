from app.platform_core.market_data.registry import MarketDataRegistry
def test_v500_alpha15_registry_seed():
    r = MarketDataRegistry().seed_defaults()
    assert "BTCUSDT" in r
    assert "IRAN_INDEX" in r
