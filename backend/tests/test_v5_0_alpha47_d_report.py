from app.platform_core.build_dashboard.report import BuildDashboardIntegrationReportService

def test_report(): assert BuildDashboardIntegrationReportService().report()['ready'] is True
