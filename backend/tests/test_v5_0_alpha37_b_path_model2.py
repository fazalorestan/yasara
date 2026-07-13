from pathlib import Path

def test_v500_alpha37_b_path_model2():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha37_broker_orders_account/models.py').exists()
