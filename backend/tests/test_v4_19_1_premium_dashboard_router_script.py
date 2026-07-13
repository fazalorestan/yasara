from pathlib import Path

def test_v4191_premium_dashboard_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_19_1_premium_dashboard_router_patch.py").exists()
