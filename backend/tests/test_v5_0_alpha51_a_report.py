from app.platform_core.windows_exe_smoke_build.report import WindowsExeSmokeBuildReportService

def test_report(): assert WindowsExeSmokeBuildReportService().report()['ready'] is True
