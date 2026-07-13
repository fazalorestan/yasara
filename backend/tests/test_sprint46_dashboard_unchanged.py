from pathlib import Path
def test_dashboard_unchanged():
    root = Path(__file__).resolve().parents[2]
    text = (root / "frontend/src/App.tsx").read_text(encoding="utf-8")
    assert "return <EnterpriseTradingOS />" in text
    assert "return <AIFirstDashboard />" not in text
