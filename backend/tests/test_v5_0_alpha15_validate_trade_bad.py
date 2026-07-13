from app.platform_core.market_data.validation import MarketDataQualityValidator
def test_v500_alpha15_validate_trade_bad():
    t = {"symbol":"BTCUSDT","price":0,"quantity":1}
    assert "invalid_price" in MarketDataQualityValidator().validate_trade(t)["errors"]
