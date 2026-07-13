from app.v22_market_engine.service import MarketDataEngineServiceV22

def test_market_engine_tick():
    t = MarketDataEngineServiceV22().tick('BTCUSDT','binance')
    assert t.symbol == 'BTCUSDT'
    assert t.price > 0
    assert t.spread > 0
