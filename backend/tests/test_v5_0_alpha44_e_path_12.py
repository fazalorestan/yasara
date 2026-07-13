from pathlib import Path

def test_path_12():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_44_pic_enterprise_patch.py').exists()
