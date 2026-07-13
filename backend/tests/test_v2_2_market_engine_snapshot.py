from app.v22_market_engine.service import MarketDataEngineServiceV22

def test_market_engine_snapshot():
    s = MarketDataEngineServiceV22().snapshot('all')
    assert s['ready'] is True
    assert s['live_trading_enabled'] is False
    assert s['source'] == 'v22_market_data_engine'
