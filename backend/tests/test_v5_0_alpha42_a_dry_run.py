from app.platform_core.execution_engine.dry_run_executor import DryRunExecutorService

def test_v500_alpha42_a_dry_run(): assert DryRunExecutorService().execute()['executed'] is False
