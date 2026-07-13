from pathlib import Path

def test_v500_alpha32_1_path_changelog():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_32_1_DEFINITIVE_PATCH_RUNNER_CHANGELOG.md').exists()
