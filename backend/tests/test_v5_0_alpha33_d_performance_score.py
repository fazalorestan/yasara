from app.platform_core.ai_decision.enterprise.performance import AIDecisionPerformanceGate

def test_v500_alpha33_d_performance_score(): assert AIDecisionPerformanceGate().evaluate()['score'] >= 9.5