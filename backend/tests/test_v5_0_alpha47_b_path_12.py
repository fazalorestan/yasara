from pathlib import Path

def test_path_12():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha47_ci_pipeline/models.py').exists()
