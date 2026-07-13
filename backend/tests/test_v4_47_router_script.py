from pathlib import Path

def test_v447_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_47_indicator_alert_notification_router_patch.py").exists()
