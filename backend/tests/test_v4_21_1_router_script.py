from pathlib import Path

def test_v4211_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_21_1_frontend_compatibility_router_patch.py").exists()
