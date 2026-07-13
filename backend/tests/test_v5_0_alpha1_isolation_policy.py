from app.platform_core.indicators.v5_expansion.isolation_policy import IndicatorIsolationPolicy

def test_v500_alpha1_isolation_policy():
 p=IndicatorIsolationPolicy().policy(); assert p['ready'] and p['execution_allowed'] is False
