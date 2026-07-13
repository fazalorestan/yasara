from pathlib import Path

def test_v500_alpha33_1_path_changelog():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_33_1_SIMPLE_PATCH_RUNNER_FIX_CHANGELOG.md').exists()
