from app.platform_core.execution_engine.enterprise.runtime_acceptance import ExecutionEnterpriseRuntimeAcceptance

def test_v500_alpha42_e_runtime_endpoints(): assert len(ExecutionEnterpriseRuntimeAcceptance().contract()['required_runtime_endpoints']) == 5
