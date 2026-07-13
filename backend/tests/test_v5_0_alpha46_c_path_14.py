from pathlib import Path

def test_path_14():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/api/v1/routes/v500_alpha46_workspace_navigation_v1.py').exists()
