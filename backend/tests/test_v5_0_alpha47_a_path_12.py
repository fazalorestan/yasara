from pathlib import Path

def test_path_12():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/build_pipeline/plugin_build_contract.py').exists()
