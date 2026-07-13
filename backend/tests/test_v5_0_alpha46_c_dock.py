from app.platform_core.desktop_app.dock_layout_manager import DesktopDockLayoutManager

def test_dock(): assert DesktopDockLayoutManager().dock_layout()['dock_enabled'] is True
