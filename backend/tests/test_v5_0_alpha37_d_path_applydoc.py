from pathlib import Path

def test_v500_alpha37_d_path_applydoc():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_37_BROKER_ENTERPRISE_PATCH.md').exists()
