from pathlib import Path

def test_v447_frontend_alert_types():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "indicators" / "yasara" / "yasara-alert-types.ts").exists()
