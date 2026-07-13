from app.platform_core.portfolio_intelligence.integration_report import PortfolioIntegrationReportService

def test_v500_alpha35_c_report(): assert PortfolioIntegrationReportService().report()['ready'] is True