from pathlib import Path

def test_path_9():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/windows_packaging/report.py').exists()
