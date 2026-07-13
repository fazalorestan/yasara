from app.v500_alpha35_portfolio_ai_optimization.service import PortfolioAIOptimizationFacadeV500Alpha35

def test_v500_alpha35_c_facade_risk_check():
 r=PortfolioAIOptimizationFacadeV500Alpha35().risk_check(); assert r is not None
