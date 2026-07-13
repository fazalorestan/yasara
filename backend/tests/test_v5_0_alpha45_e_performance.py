from app.platform_core.production_runtime.enterprise.performance import RuntimeEnterprisePerformanceGate

def test_performance(): assert RuntimeEnterprisePerformanceGate().evaluate()['score'] >= 9.5
