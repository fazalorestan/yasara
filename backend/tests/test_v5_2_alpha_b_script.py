from pathlib import Path

def test_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'scripts/build_first_real_windows_exe.py').exists()
