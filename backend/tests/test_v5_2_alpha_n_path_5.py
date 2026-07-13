from pathlib import Path

def test_path_5():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/tests/test_v5_2_alpha_n_launcher_build_sync.py').exists()
