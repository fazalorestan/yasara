from pathlib import Path

def test_v4231_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_23_1_path_resolver_router_patch.py").exists()
