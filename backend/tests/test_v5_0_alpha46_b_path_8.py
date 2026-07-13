from pathlib import Path

def test_path_8():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/desktop_app/live_dashboard_connector.py').exists()
