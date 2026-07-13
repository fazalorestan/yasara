from app.v500_alpha35_portfolio_ai_optimization.models import PortfolioAIOptimizationSummaryV500Alpha35

def test_v500_alpha35_c_summary():
 s=PortfolioAIOptimizationSummaryV500Alpha35(); assert s.ready and s.test_pack_size==50