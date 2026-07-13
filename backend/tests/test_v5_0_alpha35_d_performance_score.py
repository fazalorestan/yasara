from app.platform_core.portfolio_intelligence.enterprise.performance import PortfolioEnterprisePerformanceGate

def test_v500_alpha35_d_performance_score(): assert PortfolioEnterprisePerformanceGate().evaluate()['score'] >= 9.5