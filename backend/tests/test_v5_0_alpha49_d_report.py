from app.platform_core.windows_portable_build.report import WindowsPortableBuildReportService

def test_report(): assert WindowsPortableBuildReportService().report()['ready'] is True
