from pathlib import Path

def test_v500_alpha34_0_path_routes_folder():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/api/v1/routes/v500_alpha34_0_auto_router_registry_v1.py').exists()
