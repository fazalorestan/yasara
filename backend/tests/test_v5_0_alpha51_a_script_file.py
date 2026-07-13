from pathlib import Path

def test_script_file():
 root=Path(__file__).resolve().parents[2]; assert (root/'scripts/run_windows_exe_smoke.py').exists()
