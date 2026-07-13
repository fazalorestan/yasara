from pathlib import Path

def test_path_15():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_50_artifact_registration_patch.py').exists()
