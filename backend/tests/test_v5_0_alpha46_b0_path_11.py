from pathlib import Path

def test_path_11():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha46_core_stabilization/models.py').exists()
