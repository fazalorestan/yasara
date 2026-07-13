from app.platform_core.portfolio_intelligence.enterprise.service import PortfolioEnterpriseService

def test_v500_alpha35_d_final_status_score(): assert PortfolioEnterpriseService().final_status()['quality_score'] >= 9.5
