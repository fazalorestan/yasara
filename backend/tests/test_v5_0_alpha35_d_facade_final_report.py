from app.v500_alpha35_portfolio_enterprise.service import PortfolioEnterpriseFacadeV500Alpha35

def test_v500_alpha35_d_facade_final_report():
 r=PortfolioEnterpriseFacadeV500Alpha35().final_report(); assert r is not None
