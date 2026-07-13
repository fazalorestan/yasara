from app.platform_core.portfolio_intelligence.enterprise.security import PortfolioEnterpriseSecurityGate

def test_v500_alpha35_d_security(): assert PortfolioEnterpriseSecurityGate().evaluate()['score'] >= 9.5