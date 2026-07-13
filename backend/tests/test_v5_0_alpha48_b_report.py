from app.platform_core.windows_packaging.report import WindowsPackagingReportService

def test_report(): assert WindowsPackagingReportService().report()['ready'] is True
