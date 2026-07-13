from pathlib import Path

def test_path_10():
 root=Path(__file__).resolve().parents[2]; assert (root/"backend/scripts/apply_v5_0_alpha_46_desktop_foundation_patch.py").exists()
