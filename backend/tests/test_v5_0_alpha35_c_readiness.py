from app.platform_core.portfolio_intelligence.integration_readiness import PortfolioIntegrationReadinessGate

def test_v500_alpha35_c_readiness(): assert PortfolioIntegrationReadinessGate().run()['ready'] is True