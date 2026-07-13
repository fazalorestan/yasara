from app.v31_live_exchange.service import LiveExchangeServiceV31

def test_v31_tick():
    t = LiveExchangeServiceV31().live_tick()
    assert t["ready"] is True
    assert t["price"] > 0
    assert t["live_trading_enabled"] is False
