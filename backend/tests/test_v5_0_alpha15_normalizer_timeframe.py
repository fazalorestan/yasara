from app.platform_core.market_data.normalizer import MarketDataNormalizer
def test_v500_alpha15_normalizer_timeframe():
    assert MarketDataNormalizer().normalize_timeframe("4H") == "4h"
