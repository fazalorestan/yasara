from pathlib import Path

def test_v438_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_38_enterprise_cache_router_patch.py").exists()
