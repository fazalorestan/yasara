from pathlib import Path

def test_v500_alpha36_b_path_service():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha36_plugin_runtime_sandbox/service.py').exists()
