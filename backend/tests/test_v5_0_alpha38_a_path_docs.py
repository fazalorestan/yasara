from pathlib import Path

def test_v500_alpha38_a_path_docs():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_38/EXCHANGE_ABSTRACTION_PACKAGE_A.md').exists()
