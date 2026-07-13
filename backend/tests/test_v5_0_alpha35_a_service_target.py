from app.platform_core.portfolio_intelligence.service import PortfolioIntelligenceCoreService

def test_v500_alpha35_a_service_target(): assert PortfolioIntelligenceCoreService().target_allocation()['ready'] is True