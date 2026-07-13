from app.platform_core.portfolio_intelligence.capital_allocation import PortfolioCapitalAllocationAdvisor

def test_v500_alpha35_b_capital_block(): assert PortfolioCapitalAllocationAdvisor().advise([],100)['execution_allowed'] is False