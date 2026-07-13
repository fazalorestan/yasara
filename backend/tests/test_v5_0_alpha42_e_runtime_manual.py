from app.platform_core.execution_engine.enterprise.runtime_acceptance import ExecutionEnterpriseRuntimeAcceptance

def test_v500_alpha42_e_runtime_manual(): assert ExecutionEnterpriseRuntimeAcceptance().contract()['manual_apply_required'] is False
