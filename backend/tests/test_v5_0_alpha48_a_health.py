from app.platform_core.windows_app.app_health import WindowsAppHealthService

def test_health(): assert WindowsAppHealthService().health()['app_health']=='green'
