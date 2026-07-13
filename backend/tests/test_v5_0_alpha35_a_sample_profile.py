from app.platform_core.portfolio_intelligence.sample import PortfolioIntelligenceSampleData

def test_v500_alpha35_a_sample_profile(): assert PortfolioIntelligenceSampleData().profile()['portfolio_id']=='demo_portfolio'