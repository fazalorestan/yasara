from app.v11_market_data.event_bus import MarketEventBusV11

def test_event_bus_ticker_event():
    bus = MarketEventBusV11()
    event = bus.ticker_updated("binance", "BTCUSDT", {"last_price": 1})
    assert bus.count() == 1
    assert event.event_type.value == "ticker_updated"
