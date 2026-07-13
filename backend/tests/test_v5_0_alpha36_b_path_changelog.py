from pathlib import Path

def test_v500_alpha36_b_path_changelog():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_36_PLUGIN_RUNTIME_SANDBOX_CHANGELOG.md').exists()
