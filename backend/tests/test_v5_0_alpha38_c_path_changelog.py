from pathlib import Path

def test_v500_alpha38_c_path_changelog():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_38_EXCHANGE_CONNECTIVITY_CHANGELOG.md').exists()
