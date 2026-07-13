from app.platform_core.desktop_app.multi_workspace import DesktopMultiWorkspaceService

def test_multi(): assert DesktopMultiWorkspaceService().support()['multi_workspace_enabled'] is True
