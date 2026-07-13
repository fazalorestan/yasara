from pathlib import Path

def test_entry_file():
 root=Path(__file__).resolve().parents[2]; assert (root/'desktop/yasara_desktop.py').exists()
