from pathlib import Path

def test_path_20():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_47_build_pipeline_patch.py').exists()
