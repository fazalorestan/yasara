from app.platform_core.portfolio_intelligence.enterprise.security import PortfolioEnterpriseSecurityGate

def test_v500_alpha35_d_security_block(): assert PortfolioEnterpriseSecurityGate().evaluate()['execution_allowed'] is False