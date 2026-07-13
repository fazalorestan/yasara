from app.platform_core.native_desktop.report import NativeDesktopApplicationReportService

def test_report(): assert NativeDesktopApplicationReportService().report()['ready'] is True
