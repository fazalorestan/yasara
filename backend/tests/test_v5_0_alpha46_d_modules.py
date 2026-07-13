from app.platform_core.desktop_app.module_tracker import DesktopModuleTracker

def test_modules(): assert DesktopModuleTracker().modules()['ready'] is True
