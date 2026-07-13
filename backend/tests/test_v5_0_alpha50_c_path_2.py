from pathlib import Path

def test_path_2():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/windows_packaging_enablement/dependency_check.py').exists()
