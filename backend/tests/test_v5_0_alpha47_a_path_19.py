from pathlib import Path

def test_path_19():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/api/v1/routes/v500_alpha47_build_pipeline_v1.py').exists()
