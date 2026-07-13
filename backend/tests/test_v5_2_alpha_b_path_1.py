from pathlib import Path

def test_path_1():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/first_real_exe_build/__init__.py').exists()
