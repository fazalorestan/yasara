from app.platform_core.desktop_launcher.report import DesktopRuntimeLauncherReportService

def test_report(): assert DesktopRuntimeLauncherReportService().report()['ready'] is True
