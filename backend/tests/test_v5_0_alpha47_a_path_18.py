from pathlib import Path

def test_path_18():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha47_build_pipeline/service.py').exists()
