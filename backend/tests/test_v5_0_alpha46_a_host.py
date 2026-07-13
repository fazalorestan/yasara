from app.platform_core.desktop_app.desktop_host import DesktopHostService

def test_host(): assert DesktopHostService().status()['dashboard_connected'] is True
