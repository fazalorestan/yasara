from app.v11_market_data.cache import MarketCacheV11
from app.v11_market_data.rest_fallback import RestFallbackProviderV11

def test_market_cache_snapshot():
    cache = MarketCacheV11()
    ticker = RestFallbackProviderV11().synthetic_ticker("binance", "BTCUSDT", 50000)
    cache.update_ticker(ticker)
    snapshot = cache.snapshot()
    assert snapshot.ready is True
    assert snapshot.count == 1
    assert snapshot.items[0].spread == 1.0
