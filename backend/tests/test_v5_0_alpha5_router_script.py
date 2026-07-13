from pathlib import Path

def test_v500_alpha5_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v5_0_alpha_5_indicator_release_gate_router_patch.py").exists()
