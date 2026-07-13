from pathlib import Path

def test_v500_alpha43_a_path_changelog():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_43_BROKER_CORE_CHANGELOG.md').exists()
