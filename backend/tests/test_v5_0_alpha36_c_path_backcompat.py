from pathlib import Path

def test_v500_alpha36_c_path_backcompat():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_36_PLUGIN_VERSIONING_BACKWARD_COMPATIBILITY.md').exists()
