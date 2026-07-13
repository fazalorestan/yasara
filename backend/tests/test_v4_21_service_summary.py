from app.v421_market_structure_pro.service import MarketStructureProServiceV421

def test_v421_service_summary():
    s = MarketStructureProServiceV421().summary()
    assert s.ready is True
    assert s.constitution_compliant is True
