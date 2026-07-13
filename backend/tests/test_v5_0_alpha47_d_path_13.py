from pathlib import Path

def test_path_13():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha47_build_dashboard/service.py').exists()
