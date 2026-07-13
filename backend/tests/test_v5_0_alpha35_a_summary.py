from app.v500_alpha35_portfolio_intelligence_core.models import PortfolioIntelligenceCoreSummaryV500Alpha35

def test_v500_alpha35_a_summary():
 s=PortfolioIntelligenceCoreSummaryV500Alpha35(); assert s.ready and s.test_pack_size==50