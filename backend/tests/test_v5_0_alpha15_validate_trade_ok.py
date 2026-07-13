from app.platform_core.market_data.validation import MarketDataQualityValidator
def test_v500_alpha15_validate_trade_ok():
    t = {"symbol":"BTCUSDT","price":1,"quantity":1}
    assert MarketDataQualityValidator().validate_trade(t)["valid"] is True
