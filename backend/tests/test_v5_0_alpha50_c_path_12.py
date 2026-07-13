from pathlib import Path

def test_path_12():
 root=Path(__file__).resolve().parents[2]; assert (root/'scripts/build_windows_exe.py').exists()
