from pathlib import Path

def test_v500_alpha33_1_path_service():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha33_1_simple_patch_runner/service.py').exists()
