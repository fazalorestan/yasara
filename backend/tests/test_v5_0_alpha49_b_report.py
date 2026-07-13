from app.platform_core.desktop_gui.report import DesktopDashboardGUIShellReportService

def test_report(): assert DesktopDashboardGUIShellReportService().report()['ready'] is True
