from pathlib import Path

def test_v500_alpha36_c_path_docs2():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_36/ENTERPRISE_PLUGIN_SDK_PACKAGE_C.md').exists()
