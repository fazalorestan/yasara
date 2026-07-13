from app.platform_core.native_windows_launcher.report import NativeWindowsLauncherReportService

def test_report(): assert NativeWindowsLauncherReportService().report()['ready'] is True
