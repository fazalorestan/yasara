from app.platform_core.execution_engine.execution_metrics import ExecutionMetricsService

def test_v500_alpha42_d_metrics(): assert ExecutionMetricsService().metrics()['orders_real']==0
