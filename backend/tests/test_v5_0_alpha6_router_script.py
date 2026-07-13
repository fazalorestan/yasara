from pathlib import Path

def test_v500_alpha6_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v5_0_alpha_6_indicator_math_router_patch.py").exists()
