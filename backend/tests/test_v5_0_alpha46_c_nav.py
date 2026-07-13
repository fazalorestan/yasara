from app.platform_core.desktop_app.navigation_state import DesktopNavigationStateManager

def test_nav(): assert DesktopNavigationStateManager().state()['current_route']=='dashboard'
