from app.platform_core.desktop_app.theme_manager import DesktopThemeManager

def test_theme(): assert DesktopThemeManager().theme()['supports_dark'] is True
