from app.v22_market_engine.service import MarketDataEngineServiceV22

def test_market_engine_summary():
    s = MarketDataEngineServiceV22().summary()
    assert s.operational_progress_percent == 75
    assert s.remaining_to_full_operational_percent == 25
