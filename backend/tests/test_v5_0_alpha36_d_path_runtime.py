from pathlib import Path

def test_v500_alpha36_d_path_runtime():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/plugin_sdk/enterprise/runtime_acceptance.py').exists()
