from pathlib import Path

def test_v500_alpha43_b_path_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_43_broker_account_patch.py').exists()
