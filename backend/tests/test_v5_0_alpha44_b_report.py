from app.platform_core.project_intelligence.dashboard_report import LiveDashboardReportService

def test_report(): assert LiveDashboardReportService().report()['dashboard_backend']=='live'
