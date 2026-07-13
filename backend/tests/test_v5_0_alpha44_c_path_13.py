from pathlib import Path

def test_path_13():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_44_build_intelligence_patch.py').exists()
