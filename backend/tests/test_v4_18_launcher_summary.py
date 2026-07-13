from app.v418_launcher.models import LauncherSummaryV418

def test_v418_launcher_summary():
    s = LauncherSummaryV418()
    assert s.ready is True
    assert s.launcher_command == "python yasara.py start"
