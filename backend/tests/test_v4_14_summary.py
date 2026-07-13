from app.v414_ai_fusion.service import AIDecisionFusionServiceV414
def test_v414_summary():
    s=AIDecisionFusionServiceV414().summary()
    assert s.ready is True
    assert s.constitution_compliant is True
