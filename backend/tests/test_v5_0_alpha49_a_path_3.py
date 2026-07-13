from pathlib import Path

def test_path_3():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/native_desktop/main_window_host.py').exists()
