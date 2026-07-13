from app.v31_live_exchange.service import LiveExchangeServiceV31

def test_v31_candles():
    c = LiveExchangeServiceV31().live_candles(limit=20)
    assert c["ready"] is True
    assert len(c["candles"]) == 20
