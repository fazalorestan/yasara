from app.platform_core.desktop_app.workspace_panel import DesktopWorkspacePanelContract

def test_workspace(): assert DesktopWorkspacePanelContract().panel()['active_panel']=='dashboard_panel'
