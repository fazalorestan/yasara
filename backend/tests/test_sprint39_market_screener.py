from app.market_tools_v1.screener import MarketScreenerV1, ScreenerFilterV1, ScreenerInputItemV1

def test_market_screener_filters_change_and_volume():
    items = [
        ScreenerInputItemV1(symbol="A", price=1, change_percent=5, volume=1000),
        ScreenerInputItemV1(symbol="B", price=1, change_percent=1, volume=10),
    ]
    result = MarketScreenerV1().filter(items, ScreenerFilterV1(min_change_percent=3, min_volume=100))
    assert [i.symbol for i in result] == ["A"]
