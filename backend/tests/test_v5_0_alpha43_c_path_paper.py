from pathlib import Path

def test_v500_alpha43_c_path_paper():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/broker_layer/paper_order_contract.py').exists()
