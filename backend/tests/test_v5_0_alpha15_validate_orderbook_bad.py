from app.platform_core.market_data.validation import MarketDataQualityValidator
def test_v500_alpha15_validate_orderbook_bad():
    b = {"symbol":"BTCUSDT","bids":[{"price":0,"quantity":1}],"asks":[]}
    assert MarketDataQualityValidator().validate_orderbook(b)["valid"] is False
