from app.platform_core.desktop_app.sprint_tracker import DesktopSprintTracker

def test_sprint(): assert DesktopSprintTracker().sprint()['ready'] is True
