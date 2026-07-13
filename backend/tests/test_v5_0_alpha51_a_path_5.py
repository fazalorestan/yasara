from pathlib import Path

def test_path_5():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/windows_exe_smoke_build/failure_diagnostics.py').exists()
