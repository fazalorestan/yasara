from app.platform_core.ai_intelligence.enterprise.performance import AIEnterprisePerformanceGate

def test_v500_alpha40_e_performance_score(): assert AIEnterprisePerformanceGate().evaluate()['score'] >= 9.5
