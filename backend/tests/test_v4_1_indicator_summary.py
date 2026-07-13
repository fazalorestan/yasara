from app.v41_indicator_engine.service import ModularIndicatorEngineServiceV41

def test_v41_summary():
    s = ModularIndicatorEngineServiceV41().summary()
    assert s.product_progress_percent == 88
    assert s.constitution_compliant is True
