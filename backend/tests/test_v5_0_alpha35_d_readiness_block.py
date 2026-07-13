from app.platform_core.portfolio_intelligence.enterprise.readiness import PortfolioEnterpriseReadinessGate

def test_v500_alpha35_d_readiness_block(): assert PortfolioEnterpriseReadinessGate().run()['execution_allowed'] is False
