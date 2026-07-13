from app.platform_core.desktop_app.ui_report import DesktopUIReportService

def test_report(): assert DesktopUIReportService().report()['ready'] is True
