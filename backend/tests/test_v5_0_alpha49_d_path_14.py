from pathlib import Path

def test_path_14():
 root=Path(__file__).resolve().parents[2]; assert (root/'scripts/build_windows_portable.py').exists()
