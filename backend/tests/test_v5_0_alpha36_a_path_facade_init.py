from pathlib import Path

def test_v500_alpha36_a_path_facade_init():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha36_plugin_sdk_core/__init__.py').exists()
