from app.platform_core.broker_layer.enterprise.performance import BrokerEnterprisePerformanceGate

def test_v500_alpha37_d_performance_score(): assert BrokerEnterprisePerformanceGate().evaluate()['score'] >= 9.5