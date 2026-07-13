from app.platform_core.desktop_app.workspace_manager import DesktopWorkspaceManager

def test_workspace(): assert DesktopWorkspaceManager().workspace()['dashboard_workspace_enabled'] is True
