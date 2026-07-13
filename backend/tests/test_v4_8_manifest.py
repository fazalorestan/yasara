from app.v48_production_readiness.service import ProductionReadinessServiceV48

def test_v48_manifest():
    data = ProductionReadinessServiceV48().manifest()
    assert data["ready"] is True
    assert "commercial_excludes" in data["manifest"]
