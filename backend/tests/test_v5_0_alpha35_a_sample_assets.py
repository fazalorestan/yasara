from app.platform_core.portfolio_intelligence.sample import PortfolioIntelligenceSampleData

def test_v500_alpha35_a_sample_assets(): assert len(PortfolioIntelligenceSampleData().assets()) == 3