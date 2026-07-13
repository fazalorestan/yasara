from pathlib import Path

def test_v500_alpha37_b_path_docs2():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_37/BROKER_ABSTRACTION_PACKAGE_B.md').exists()
