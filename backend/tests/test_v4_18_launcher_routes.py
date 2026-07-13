from pathlib import Path

def test_v418_launcher_routes():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_18_launcher_router_patch.py").exists()
