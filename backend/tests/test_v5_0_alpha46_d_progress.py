from app.platform_core.desktop_app.project_progress_engine import DesktopProjectProgressEngine

def test_progress(): assert DesktopProjectProgressEngine().progress()['overall'] >= 0
