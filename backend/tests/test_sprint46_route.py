from pathlib import Path
def test_route():
    root = Path(__file__).resolve().parents[2]
    text = (root / "backend/app/api/v1/routes/v52_enterprise_workspaces_v1.py").read_text(encoding="utf-8")
    assert 'prefix="/enterprise/workspaces"' in text
