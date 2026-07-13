from pathlib import Path

def test_v500_alpha43_a_path_adapter():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/broker_layer/broker_adapter_contract.py').exists()
