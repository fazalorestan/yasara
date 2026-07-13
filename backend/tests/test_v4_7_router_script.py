from pathlib import Path

def test_v47_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_7_notification_alerts_router_patch.py").exists()
