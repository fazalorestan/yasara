from app.platform_core.portfolio_intelligence.integration_report import PortfolioIntegrationReportService

def test_v500_alpha35_c_report_has_risk(): assert 'risk_link' in PortfolioIntegrationReportService().report()
