from pathlib import Path

def test_path_11():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/windows_app/readiness.py').exists()
