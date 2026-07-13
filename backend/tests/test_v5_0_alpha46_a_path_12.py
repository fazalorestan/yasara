from pathlib import Path

def test_path_12():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha46_desktop_host/__init__.py').exists()
