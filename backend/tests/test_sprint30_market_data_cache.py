from app.multi_exchange_v1.cache import MarketDataCacheV1

def test_market_data_cache_set_get():
    cache = MarketDataCacheV1(ttl_seconds=10)
    cache.set("ticker:BTCUSDT", {"price": 100})
    assert cache.get("ticker:BTCUSDT")["price"] == 100
    assert cache.size() == 1

def test_market_data_cache_clear():
    cache = MarketDataCacheV1()
    cache.set("x", 1)
    cache.clear()
    assert cache.get("x") is None
