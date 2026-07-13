from app.platform_core.portfolio_intelligence.readiness import PortfolioIntelligenceReadinessGate

def test_v500_alpha35_a_readiness_block(): assert PortfolioIntelligenceReadinessGate().run()['execution_allowed'] is False