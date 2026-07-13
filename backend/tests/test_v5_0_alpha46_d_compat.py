from app.platform_core.desktop_app.dashboard_intelligence_report import DesktopDashboardIntelligenceReport, desktop_dashboard_intelligence_report

def test_compat(): assert DesktopDashboardIntelligenceReport().report()['ready'] and desktop_dashboard_intelligence_report.report()['ready']
