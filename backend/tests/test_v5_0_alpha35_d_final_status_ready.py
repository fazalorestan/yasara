from app.platform_core.portfolio_intelligence.enterprise.service import PortfolioEnterpriseService

def test_v500_alpha35_d_final_status_ready(): assert PortfolioEnterpriseService().final_status()['ready'] is True
