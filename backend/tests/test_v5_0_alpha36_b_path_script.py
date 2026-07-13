from pathlib import Path

def test_v500_alpha36_b_path_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_36_plugin_runtime_sandbox_patch.py').exists()
