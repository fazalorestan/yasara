from app.platform_core.desktop_app.desktop_health import DesktopHealthContract

def test_health(): assert DesktopHealthContract().health()['desktop_health']=='green'
