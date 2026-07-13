from pathlib import Path

def test_v500_alpha1_docs():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_1'/'INDICATOR_EXPANSION_FOUNDATION.md').exists()
