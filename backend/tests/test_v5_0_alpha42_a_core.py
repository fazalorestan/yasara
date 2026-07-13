from app.platform_core.execution_engine.execution_core import ExecutionCoreService

def test_v500_alpha42_a_core(): assert ExecutionCoreService().status()['mode']=='dry_run_only'
