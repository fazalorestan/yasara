from app.platform_core.desktop_app.workspace_report import DesktopWorkspaceReport, desktop_workspace_report

def test_compat(): assert DesktopWorkspaceReport().report()['ready'] and desktop_workspace_report.report()['ready']
