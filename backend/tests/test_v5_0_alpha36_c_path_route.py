from pathlib import Path

def test_v500_alpha36_c_path_route():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/api/v1/routes/v500_alpha36_plugin_versioning_v1.py').exists()
