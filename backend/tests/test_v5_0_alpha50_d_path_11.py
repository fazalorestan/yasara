from pathlib import Path

def test_path_11():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha50_artifact_registration/models.py').exists()
