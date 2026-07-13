from app.platform_core.desktop_app.workspace_readiness import DesktopWorkspaceReadinessGate

def test_readiness(): assert DesktopWorkspaceReadinessGate().run()['ready'] is True
