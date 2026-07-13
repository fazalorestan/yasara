from pathlib import Path

def test_path_14():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha49_desktop_gui/service.py').exists()
