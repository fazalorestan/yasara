from app.platform_core.desktop_gui.navigation_shell import DesktopNavigationShellContract

def test_navigation(): assert 'dashboard' in DesktopNavigationShellContract().navigation()['items']
