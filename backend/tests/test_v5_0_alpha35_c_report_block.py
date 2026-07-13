from app.platform_core.portfolio_intelligence.integration_report import PortfolioIntegrationReportService

def test_v500_alpha35_c_report_block(): assert PortfolioIntegrationReportService().report()['execution_allowed'] is False