from pathlib import Path

def test_v500_alpha36_d_path_model():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha36_plugin_enterprise/models.py').exists()
