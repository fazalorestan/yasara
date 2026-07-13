from app.platform_core.desktop_app.desktop_bootstrap import DesktopBootstrapService

def test_bootstrap(): assert DesktopBootstrapService().bootstrap()['bootstrapped'] is True
