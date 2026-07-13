from app.platform_core.windows_exe_build.report import WindowsExeBuildScriptReportService

def test_report(): assert WindowsExeBuildScriptReportService().report()['ready'] is True
