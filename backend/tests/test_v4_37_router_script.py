from pathlib import Path

def test_v437_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_37_enterprise_queue_router_patch.py").exists()
