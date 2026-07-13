from app.platform_core.project_intelligence.desktop_dashboard_report import DesktopDashboardReportService

def test_report(): assert DesktopDashboardReportService().report()['desktop_shell_ready'] is True
