from pathlib import Path

def test_v500_alpha39_a_path_docs():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_39/LIVE_DATA_PIPELINE_PACKAGE_A.md').exists()
