from app.platform_core.market_data.validation import MarketDataQualityValidator
def test_v500_alpha15_validate_orderbook_ok():
    b = {"symbol":"BTCUSDT","bids":[{"price":1,"quantity":1}],"asks":[{"price":2,"quantity":1}]}
    assert MarketDataQualityValidator().validate_orderbook(b)["valid"] is True
