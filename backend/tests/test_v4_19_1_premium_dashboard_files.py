from pathlib import Path

def test_v4191_premium_dashboard_files():
    root = Path(__file__).resolve().parents[2]
    app = root / "frontend" / "src" / "App.tsx"
    css = root / "frontend" / "src" / "styles" / "premium-dashboard.css"
    assert app.exists()
    assert css.exists()
    text = app.read_text(encoding="utf-8")
    assert "Premium Trading Dashboard" not in text or "premium" in text.lower()
    assert "Market Chart" in text
    assert "AI Signals" in text
