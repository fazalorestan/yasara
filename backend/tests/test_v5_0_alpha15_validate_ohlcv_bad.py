from app.platform_core.market_data.validation import MarketDataQualityValidator
def test_v500_alpha15_validate_ohlcv_bad():
    c = {"symbol":"BTCUSDT","timeframe":"1h","open_time":1,"open":1,"high":1,"low":2,"close":2,"volume":10}
    assert "high_less_than_low" in MarketDataQualityValidator().validate_ohlcv(c)["errors"]
