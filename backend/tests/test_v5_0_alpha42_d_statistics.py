from app.platform_core.execution_engine.execution_statistics import ExecutionStatisticsService

def test_v500_alpha42_d_statistics(): assert ExecutionStatisticsService().statistics()['real_execution_ratio']==0.0
