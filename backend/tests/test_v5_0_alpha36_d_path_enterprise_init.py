from pathlib import Path

def test_v500_alpha36_d_path_enterprise_init():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/plugin_sdk/enterprise/__init__.py').exists()
