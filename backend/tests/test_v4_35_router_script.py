from pathlib import Path

def test_v435_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_35_configuration_center_router_patch.py").exists()
