from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_47/CI_AUTOMATED_TEST_PIPELINE_PACKAGE_B.md').exists()
