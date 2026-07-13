from pathlib import Path

def test_v500_alpha3_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v5_0_alpha_3_indicator_sandbox_router_patch.py").exists()
