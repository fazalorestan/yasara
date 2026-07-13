from pathlib import Path

def test_v427_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_27_extension_host_router_patch.py").exists()
