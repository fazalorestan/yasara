from pathlib import Path

def test_v500_alpha36_c_path_service():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha36_plugin_versioning/service.py').exists()
