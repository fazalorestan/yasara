from app.v48_production_readiness.service import ProductionReadinessServiceV48

def test_v48_summary():
    s = ProductionReadinessServiceV48().summary()
    assert s.product_progress_percent == 99
    assert s.constitution_compliant is True
