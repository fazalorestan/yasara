from pathlib import Path

def test_v500_alpha36_a_path_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_36_plugin_sdk_core_patch.py').exists()
