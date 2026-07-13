from app.platform_core.desktop_app.dashboard_intelligence_report import DesktopDashboardIntelligenceReportService

def test_report(): assert DesktopDashboardIntelligenceReportService().report()['ready'] is True
