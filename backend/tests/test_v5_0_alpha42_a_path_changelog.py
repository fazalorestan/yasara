from pathlib import Path

def test_v500_alpha42_a_path_changelog():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_42_EXECUTION_CORE_CHANGELOG.md').exists()
