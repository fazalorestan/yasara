from app.platform_core.live_data_pipeline.enterprise.performance import LiveDataEnterprisePerformanceGate

def test_v500_alpha39_e_performance(): assert LiveDataEnterprisePerformanceGate().evaluate()['ready'] is True
