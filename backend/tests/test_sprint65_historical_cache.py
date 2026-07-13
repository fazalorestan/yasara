from app.connectivity_v1.historical_cache import HistoricalCacheV1

def test_historical_cache_append():
    cache = HistoricalCacheV1()
    cache.put("BTC:1h", [{"close": 1}])
    cache.append("BTC:1h", [{"close": 2}])
    assert len(cache.get("BTC:1h").rows) == 2
