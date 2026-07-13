from pathlib import Path

def test_path_9():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha51_exe_smoke_build/__init__.py').exists()
