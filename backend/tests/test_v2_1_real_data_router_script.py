from pathlib import Path

def test_real_data_router_script_exists():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v2_1_real_data_activation_router_patch.py").exists()
