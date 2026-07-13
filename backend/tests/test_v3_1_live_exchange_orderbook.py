from app.v31_live_exchange.service import LiveExchangeServiceV31

def test_v31_orderbook():
    ob = LiveExchangeServiceV31().live_orderbook()
    assert ob["ready"] is True
    assert len(ob["asks"]) > 0
    assert len(ob["bids"]) > 0
