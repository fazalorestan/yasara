from app.v500_alpha44_build_intelligence.service import BuildIntelligenceFacadeV500Alpha44

def test_facade_report():
 r=BuildIntelligenceFacadeV500Alpha44().report(); assert r is not None
