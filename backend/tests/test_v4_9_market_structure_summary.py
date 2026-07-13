from app.v49_market_structure.service import ProfessionalMarketStructureServiceV49

def test_v49_summary():
    s = ProfessionalMarketStructureServiceV49().summary()
    assert s.ready is True
    assert s.constitution_compliant is True
