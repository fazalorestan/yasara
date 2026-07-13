from app.platform_core.desktop_app.status_bar import DesktopStatusBarService

def test_status(): assert DesktopStatusBarService().status_bar()['live_status_enabled'] is True
