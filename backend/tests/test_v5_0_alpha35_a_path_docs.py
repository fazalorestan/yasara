from pathlib import Path

def test_v500_alpha35_a_path_docs():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_35/PORTFOLIO_INTELLIGENCE_PACKAGE_A.md').exists()
