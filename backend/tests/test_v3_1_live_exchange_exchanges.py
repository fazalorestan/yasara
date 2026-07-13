from app.v31_live_exchange.service import LiveExchangeServiceV31

def test_v31_exchanges():
    data = LiveExchangeServiceV31().supported_exchanges()
    assert data["ready"] is True
    assert len(data["exchanges"]) >= 3
    assert data["live_trading_enabled"] is False
