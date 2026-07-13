from app.platform_core.execution_engine.report import ExecutionCoreReport

def test_v500_alpha42_a_report(): assert ExecutionCoreReport().report()['ready'] is True
