from app.platform_core.market_data.validation import MarketDataQualityValidator
def test_v500_alpha15_validate_ohlcv_ok():
    c = {"symbol":"BTCUSDT","timeframe":"1h","open_time":1,"open":1,"high":2,"low":1,"close":2,"volume":10}
    assert MarketDataQualityValidator().validate_ohlcv(c)["valid"] is True
