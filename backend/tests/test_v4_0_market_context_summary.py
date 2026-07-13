from app.v40_market_context.service import MarketContextServiceV40

def test_v40_summary():
    s = MarketContextServiceV40().summary()
    assert s.product_progress_percent == 86
    assert s.constitution_compliant is True
