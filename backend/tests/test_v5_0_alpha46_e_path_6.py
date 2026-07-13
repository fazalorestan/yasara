from pathlib import Path

def test_path_6():
 root=Path(__file__).resolve().parents[2]; assert (root/"backend/app/v500_alpha46_desktop_foundation/__init__.py").exists()
