from app.platform_core.desktop_app.workspace_report import DesktopWorkspaceReportService

def test_report(): assert DesktopWorkspaceReportService().report()['ready'] is True
