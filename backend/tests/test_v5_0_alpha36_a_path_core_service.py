from pathlib import Path

def test_v500_alpha36_a_path_core_service():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/plugin_sdk/service.py').exists()
