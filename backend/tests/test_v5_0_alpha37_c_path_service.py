from pathlib import Path

def test_v500_alpha37_c_path_service():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha37_broker_connectivity/service.py').exists()
