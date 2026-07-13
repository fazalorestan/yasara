from app.v11_market_data.symbol_registry import SymbolRegistryV11

def test_symbol_registry_normalization():
    registry = SymbolRegistryV11()
    assert registry.normalize("BTC-USDT") == "BTCUSDT"
    assert registry.normalize("BTC_USDT") == "BTCUSDT"
    assert registry.exchange_symbol("bitunix", "BTCUSDT") == "BTC-USDT"
