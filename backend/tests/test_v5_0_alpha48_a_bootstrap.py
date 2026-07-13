from app.platform_core.windows_app.app_bootstrap import WindowsAppBootstrapService

def test_bootstrap(): assert WindowsAppBootstrapService().bootstrap()['ready'] is True
