from app.platform_core.market_data.models import MarketSymbol
def test_v500_alpha15_models_symbol():
    s = MarketSymbol(symbol="BTCUSDT", base_asset="BTC", quote_asset="USDT")
    assert s.symbol == "BTCUSDT"
    assert s.enabled is True
