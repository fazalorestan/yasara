from app.v500_alpha44_build_intelligence.service import BuildIntelligenceFacadeV500Alpha44

def test_facade_state_store():
 r=BuildIntelligenceFacadeV500Alpha44().state_store(); assert r is not None
