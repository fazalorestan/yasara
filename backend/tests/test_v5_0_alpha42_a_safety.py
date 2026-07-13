from app.platform_core.execution_engine.execution_safety import ExecutionSafetyPolicy

def test_v500_alpha42_a_safety(): assert ExecutionSafetyPolicy().policy()['dry_run_only'] is True
