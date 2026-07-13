from pathlib import Path

def test_path_12():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_45_runtime_services_patch.py').exists()
