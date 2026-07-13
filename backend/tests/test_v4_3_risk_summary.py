from app.v43_risk_engine.service import AdvancedRiskEngineServiceV43

def test_v43_summary():
    s = AdvancedRiskEngineServiceV43().summary()
    assert s.product_progress_percent == 92
    assert s.constitution_compliant is True
