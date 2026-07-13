from pathlib import Path

def test_v500_alpha36_c_path_script2():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_36_plugin_versioning_patch.py').exists()
