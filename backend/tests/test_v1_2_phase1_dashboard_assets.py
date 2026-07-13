from pathlib import Path

def test_dashboard_static_assets_exist():
    root = Path(__file__).resolve().parents[1]
    assert (root / "app" / "static" / "dashboard" / "index.html").exists()
    assert (root / "app" / "static" / "dashboard" / "styles.css").exists()
    assert (root / "app" / "static" / "dashboard" / "app.js").exists()
