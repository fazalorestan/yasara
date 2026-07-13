from pathlib import Path

def test_v500_alpha38_b_path_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_38_exchange_market_data_patch.py').exists()
