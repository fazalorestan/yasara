from pathlib import Path

def test_v432_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_32_platform_versioning_router_patch.py").exists()
