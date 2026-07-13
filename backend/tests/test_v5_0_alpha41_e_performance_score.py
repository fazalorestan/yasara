from app.platform_core.strategy_engine.enterprise.performance import StrategyEnterprisePerformanceGate

def test_v500_alpha41_e_performance_score(): assert StrategyEnterprisePerformanceGate().evaluate()['score'] >= 9.5
