from app.platform_core.execution_engine.enterprise.readiness import ExecutionEnterpriseReadinessGate

def test_v500_alpha42_e_readiness_block(): assert ExecutionEnterpriseReadinessGate().run()['execution_allowed'] is False
