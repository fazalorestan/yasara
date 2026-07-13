from pathlib import Path

def test_v500_alpha40_e_path_docs_again():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_40/AI_INTELLIGENCE_PACKAGE_E.md').exists()
