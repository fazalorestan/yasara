from app.platform_core.execution_engine.readiness import ExecutionCoreReadinessGate

def test_v500_alpha42_a_readiness(): assert ExecutionCoreReadinessGate().run()['ready'] is True
