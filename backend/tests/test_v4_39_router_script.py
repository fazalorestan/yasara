from pathlib import Path

def test_v439_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_39_enterprise_storage_router_patch.py").exists()
