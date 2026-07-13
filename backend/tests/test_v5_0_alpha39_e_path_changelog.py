from pathlib import Path

def test_v500_alpha39_e_path_changelog():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_39_LIVE_DATA_ENTERPRISE_CHANGELOG.md').exists()
