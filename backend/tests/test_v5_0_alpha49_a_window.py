from app.platform_core.native_desktop.main_window_host import NativeMainWindowHost

def test_window(): assert NativeMainWindowHost().configuration()['auto_trading_enabled_default'] is False
