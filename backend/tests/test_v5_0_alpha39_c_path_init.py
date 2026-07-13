from pathlib import Path

def test_v500_alpha39_c_path_init():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha39_live_stream_manager/__init__.py').exists()
