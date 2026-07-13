from app.platform_core.portfolio_intelligence.enterprise.report import PortfolioEnterpriseReportBuilder

def test_v500_alpha35_d_report_real(): assert PortfolioEnterpriseReportBuilder().build()['real_execution_enabled'] is False