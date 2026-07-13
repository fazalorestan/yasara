from app.platform_core.market_data.normalizer import MarketDataNormalizer
def test_v500_alpha15_normalizer_symbol():
    assert MarketDataNormalizer().normalize_symbol("btc/usdt") == "BTCUSDT"
