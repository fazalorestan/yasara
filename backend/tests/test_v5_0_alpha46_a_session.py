from app.platform_core.desktop_app.desktop_session import DesktopSessionManager

def test_session(): assert DesktopSessionManager().session()['active'] is True
