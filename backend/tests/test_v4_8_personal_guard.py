from app.v48_production_readiness.models import BuildProfileRequestV48
from app.v48_production_readiness.service import ProductionReadinessServiceV48

def test_v48_personal_guard():
    data = ProductionReadinessServiceV48().build_profile_guard(BuildProfileRequestV48(build_type="personal"))
    assert data["execution_engine_allowed_future"] is True
    assert data["requires_kill_switch"] is True
