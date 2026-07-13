from pathlib import Path

def test_v500_alpha34_0_path_package_init():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha34_0_auto_router_registry/__init__.py').exists()
