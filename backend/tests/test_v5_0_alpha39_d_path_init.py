from pathlib import Path

def test_v500_alpha39_d_path_init():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha39_live_data_cache/__init__.py').exists()
