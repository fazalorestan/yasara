from app.platform_core.portfolio_intelligence.capital_allocation import PortfolioCapitalAllocationAdvisor

def test_v500_alpha35_b_capital_alloc(): assert PortfolioCapitalAllocationAdvisor().advise([{'symbol':'A','target_weight':.6,'current_weight':.3}],100)['allocations'][0]['suggested_cash']==100