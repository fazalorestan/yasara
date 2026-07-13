from pathlib import Path

def test_v500_alpha36_b_path_docs():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_36/ENTERPRISE_PLUGIN_SDK_PACKAGE_B.md').exists()
