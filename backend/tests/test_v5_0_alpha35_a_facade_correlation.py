from app.v500_alpha35_portfolio_intelligence_core.service import PortfolioIntelligenceCoreFacadeV500Alpha35

def test_v500_alpha35_a_facade_correlation():
 r=PortfolioIntelligenceCoreFacadeV500Alpha35().correlation(); assert r is not None
