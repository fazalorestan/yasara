from app.platform_core.execution_engine.analytics_report import ExecutionAnalyticsReport

def test_v500_alpha42_d_report(): assert ExecutionAnalyticsReport().report()['ready'] is True
