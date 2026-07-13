from pathlib import Path

def test_v500_alpha36_d_path_applydoc():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_36_PLUGIN_ENTERPRISE_PATCH.md').exists()
