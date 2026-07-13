from pathlib import Path

def test_v500_alpha38_c_path_init():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha38_exchange_connectivity/__init__.py').exists()
