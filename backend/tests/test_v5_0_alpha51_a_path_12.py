from pathlib import Path

def test_path_12():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/api/v1/routes/v500_alpha51_exe_smoke_build_v1.py').exists()
