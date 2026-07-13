from pathlib import Path

def test_v500_alpha35_a_path_applydoc():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_35_PORTFOLIO_INTELLIGENCE_CORE_PATCH.md').exists()
