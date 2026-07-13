from app.platform_core.portfolio_intelligence.enterprise.report import PortfolioEnterpriseReportBuilder

def test_v500_alpha35_d_report(): assert PortfolioEnterpriseReportBuilder().build()['ready'] is True