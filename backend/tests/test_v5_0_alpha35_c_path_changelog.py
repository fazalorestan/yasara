from pathlib import Path

def test_v500_alpha35_c_path_changelog():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_35_PORTFOLIO_AI_OPTIMIZATION_CHANGELOG.md').exists()
