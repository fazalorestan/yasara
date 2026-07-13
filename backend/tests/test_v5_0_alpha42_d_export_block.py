from app.platform_core.execution_engine.analytics_safety import ExecutionAnalyticsSafetyPolicy

def test_v500_alpha42_d_export_block(): assert ExecutionAnalyticsSafetyPolicy().can_export_sensitive_audit()['allowed'] is False
