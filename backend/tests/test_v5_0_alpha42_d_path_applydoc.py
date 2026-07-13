from pathlib import Path

def test_v500_alpha42_d_path_applydoc():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_42_EXECUTION_ANALYTICS_PATCH.md').exists()
