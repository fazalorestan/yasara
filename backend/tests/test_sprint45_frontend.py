from pathlib import Path
def test_frontend():
    root = Path(__file__).resolve().parents[2]
    text = (root / "frontend/src/components/enterprise/AIFirstDashboard.tsx").read_text(encoding="utf-8")
    assert "Real backend data only" in text
    assert "mock" not in text.lower()
