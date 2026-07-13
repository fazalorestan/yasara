from app.platform_core.project_intelligence.desktop_dashboard_report import DesktopDashboardReport, desktop_dashboard_report

def test_compat(): assert DesktopDashboardReport().report()['ready'] and desktop_dashboard_report.report()['ready']
