from app.platform_core.desktop_app.toolbar_manager import DesktopToolbarManager

def test_toolbar(): assert DesktopToolbarManager().toolbar()['dangerous_actions_enabled'] is False
