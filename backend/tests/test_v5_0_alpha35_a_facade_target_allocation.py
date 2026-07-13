from app.v500_alpha35_portfolio_intelligence_core.service import PortfolioIntelligenceCoreFacadeV500Alpha35

def test_v500_alpha35_a_facade_target_allocation():
 r=PortfolioIntelligenceCoreFacadeV500Alpha35().target_allocation(); assert r is not None
