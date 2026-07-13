from pathlib import Path

def test_v500_alpha43_a_path_facade_init():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha43_broker_core/__init__.py').exists()
