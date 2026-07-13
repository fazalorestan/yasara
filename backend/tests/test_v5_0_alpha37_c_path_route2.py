from pathlib import Path

def test_v500_alpha37_c_path_route2():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/api/v1/routes/v500_alpha37_broker_connectivity_v1.py').exists()
