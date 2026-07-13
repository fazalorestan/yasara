from app.platform_core.desktop_app.window_state_persistence import DesktopWindowStatePersistence

def test_window_state(): assert DesktopWindowStatePersistence().state()['backup_before_write_required'] is True
