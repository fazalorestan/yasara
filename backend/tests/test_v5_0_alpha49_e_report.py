from app.platform_core.desktop_finalization.report import InternalDesktopBuildFinalizationReportService

def test_report(): assert InternalDesktopBuildFinalizationReportService().report()['ready'] is True
