from app.v31_live_exchange.service import LiveExchangeServiceV31

def test_v31_summary():
    s = LiveExchangeServiceV31().summary()
    assert s.product_progress_percent == 48
    assert s.remaining_to_professional_product_percent == 52
