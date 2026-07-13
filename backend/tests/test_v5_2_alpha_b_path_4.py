from pathlib import Path

def test_path_4():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v52_alpha_first_real_exe_build/__init__.py').exists()
