from pathlib import Path

def test_path_17():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_49_desktop_launcher_patch.py').exists()
