from app.platform_core.native_desktop.health import NativeDesktopHealthService

def test_health(): assert NativeDesktopHealthService().health()['auto_trading_enabled'] is False
