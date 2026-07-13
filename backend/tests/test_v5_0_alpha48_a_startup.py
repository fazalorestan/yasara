from app.platform_core.windows_app.startup_flow import WindowsDesktopStartupFlow

def test_startup(): assert WindowsDesktopStartupFlow().flow()['auto_trading_enabled_default'] is False
