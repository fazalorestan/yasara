from app.platform_core.portfolio_intelligence.enterprise.security import PortfolioEnterpriseSecurityGate

def test_v500_alpha35_d_security_checks(): assert PortfolioEnterpriseSecurityGate().evaluate()['checks']['real_execution_blocked'] is True