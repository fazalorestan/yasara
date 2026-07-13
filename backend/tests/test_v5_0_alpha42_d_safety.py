from app.platform_core.execution_engine.analytics_safety import ExecutionAnalyticsSafetyPolicy

def test_v500_alpha42_d_safety(): assert ExecutionAnalyticsSafetyPolicy().policy()['analytics_only'] is True
