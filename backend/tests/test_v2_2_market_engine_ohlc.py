from app.v22_market_engine.service import MarketDataEngineServiceV22

def test_market_engine_ohlc():
    d = MarketDataEngineServiceV22().ohlc('BTCUSDT','binance','4H',20)
    assert d.ready is True
    assert len(d.candles) == 20
    assert d.candles[0].high >= d.candles[0].low
