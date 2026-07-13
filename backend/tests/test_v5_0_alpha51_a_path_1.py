from pathlib import Path

def test_path_1():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/windows_exe_smoke_build/__init__.py').exists()
