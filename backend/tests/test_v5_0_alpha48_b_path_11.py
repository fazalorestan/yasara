from pathlib import Path

def test_path_11():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha48_windows_packaging/__init__.py').exists()
