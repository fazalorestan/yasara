from app.v500_alpha35_portfolio_enterprise.models import PortfolioEnterpriseSummaryV500Alpha35

def test_v500_alpha35_d_summary():
 s=PortfolioEnterpriseSummaryV500Alpha35(); assert s.ready and s.test_pack_size==55