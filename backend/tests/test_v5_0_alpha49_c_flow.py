from app.platform_core.desktop_launcher.launch_flow import DesktopLaunchFlow

def test_flow(): assert DesktopLaunchFlow().flow()['auto_trading_enabled_default'] is False
