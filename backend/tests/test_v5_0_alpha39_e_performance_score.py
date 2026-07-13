from app.platform_core.live_data_pipeline.enterprise.performance import LiveDataEnterprisePerformanceGate

def test_v500_alpha39_e_performance_score(): assert LiveDataEnterprisePerformanceGate().evaluate()['score'] >= 9.5
