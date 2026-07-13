from app.platform_core.desktop_app.window_manager import DesktopWindowManager

def test_window(): assert DesktopWindowManager().window()['main_window'] is True
