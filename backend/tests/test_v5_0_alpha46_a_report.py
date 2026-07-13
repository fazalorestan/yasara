from app.platform_core.desktop_app.desktop_report import DesktopHostReportService

def test_report(): assert DesktopHostReportService().report()['ready'] is True
