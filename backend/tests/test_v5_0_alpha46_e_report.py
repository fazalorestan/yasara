from app.platform_core.desktop_app.foundation_report import DesktopFoundationReportService

def test_report(): assert DesktopFoundationReportService().report()["ready"] is True
