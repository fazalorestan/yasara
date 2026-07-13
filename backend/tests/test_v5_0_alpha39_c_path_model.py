from pathlib import Path

def test_v500_alpha39_c_path_model():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha39_live_stream_manager/models.py').exists()
