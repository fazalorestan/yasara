from app.platform_core.portfolio_intelligence.integration_readiness import PortfolioIntegrationReadinessGate

def test_v500_alpha35_c_readiness_block(): assert PortfolioIntegrationReadinessGate().run()['execution_allowed'] is False