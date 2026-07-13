from pathlib import Path

def test_v500_alpha43_c_path_applydoc():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_43_BROKER_ORDER_PATCH.md').exists()
