from app.platform_core.desktop_app.navigation_shell import DesktopNavigationShell

def test_navigation(): assert DesktopNavigationShell().navigation()['default_route']=='dashboard'
