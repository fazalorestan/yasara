from pathlib import Path

def test_v500_alpha43_b_path_readiness():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/broker_layer/account_readiness.py').exists()
