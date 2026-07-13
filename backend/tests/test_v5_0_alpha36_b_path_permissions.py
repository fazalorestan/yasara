from pathlib import Path

def test_v500_alpha36_b_path_permissions():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/plugin_sdk/permissions.py').exists()
