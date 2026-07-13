from app.platform_core.plugin_sdk.enterprise.performance import PluginEnterprisePerformanceGate

def test_v500_alpha36_d_performance_score(): assert PluginEnterprisePerformanceGate().evaluate()['score'] >= 9.5
