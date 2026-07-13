from app.v500_alpha35_portfolio_analytics_risk.models import PortfolioAnalyticsRiskSummaryV500Alpha35

def test_v500_alpha35_b_summary():
 s=PortfolioAnalyticsRiskSummaryV500Alpha35(); assert s.ready and s.test_pack_size==50