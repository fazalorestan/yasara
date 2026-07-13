from app.v21_real_data.service import RealDataActivationServiceV21

def test_real_data_market_snapshot():
    snapshot = RealDataActivationServiceV21().market_snapshot("all")
    assert snapshot["ready"] is True
    assert snapshot["live_trading_enabled"] is False
    assert snapshot["count"] >= 1
