from app.v48_production_readiness.models import BuildProfileRequestV48
from app.v48_production_readiness.service import ProductionReadinessServiceV48

def test_v48_commercial_guard():
    data = ProductionReadinessServiceV48().build_profile_guard(BuildProfileRequestV48(build_type="commercial"))
    assert data["execution_engine_allowed"] is False
    assert data["trade_api_keys_allowed"] is False
