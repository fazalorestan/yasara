from pathlib import Path

def test_v36_scripts():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v3_6_phase_a_meta_ykb_router_patch.py").exists()
    assert (root / "scripts" / "validate_v3_6_phase_a_meta_ykb.py").exists()
