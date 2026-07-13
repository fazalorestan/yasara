from app.v410_market_structure_sprint2.service import MarketStructureSprint2ServiceV410

def test_v410_summary():
    s=MarketStructureSprint2ServiceV410().summary(); assert s.ready is True; assert s.constitution_compliant is True
