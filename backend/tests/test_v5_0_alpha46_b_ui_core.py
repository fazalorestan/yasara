from app.platform_core.desktop_app.ui_core import DesktopUICoreService

def test_ui_core(): assert DesktopUICoreService().status()['connected_to_desktop_host'] is True
