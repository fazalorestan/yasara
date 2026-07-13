from pathlib import Path

def test_v500_alpha37_b_path_script2():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_37_broker_orders_account_patch.py').exists()
