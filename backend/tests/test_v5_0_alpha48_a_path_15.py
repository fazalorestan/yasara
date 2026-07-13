from pathlib import Path

def test_path_15():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/api/v1/routes/v500_alpha48_windows_app_v1.py').exists()
