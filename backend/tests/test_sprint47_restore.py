from pathlib import Path
def test_restore():
    root=Path(__file__).resolve().parents[2]
    text=(root/"scripts/restore_approved_dashboard_sprint47.py").read_text(encoding="utf-8")
    for token in ["Market Workspace","AI Decision Engine","Risk Panel","Portfolio Allocation"]:
        assert token in text
