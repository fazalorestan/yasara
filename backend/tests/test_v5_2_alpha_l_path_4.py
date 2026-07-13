from pathlib import Path

def test_path_4():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/tests/test_v5_2_alpha_k_force_merge_marker.py').exists()
