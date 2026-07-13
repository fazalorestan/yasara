from pathlib import Path

def test_v500_alpha43_c_path_facade_init():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha43_broker_order/__init__.py').exists()
