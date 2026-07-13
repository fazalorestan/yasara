from app.platform_core.execution_engine.enterprise.service import ExecutionEnterpriseService

def test_v500_alpha42_e_service_security():
 r=ExecutionEnterpriseService().security(); assert r is not None
