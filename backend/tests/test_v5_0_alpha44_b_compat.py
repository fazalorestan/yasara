from app.platform_core.project_intelligence.dashboard_report import LiveDashboardReport, live_dashboard_report

def test_compat(): assert LiveDashboardReport().report()['ready'] and live_dashboard_report.report()['ready']
