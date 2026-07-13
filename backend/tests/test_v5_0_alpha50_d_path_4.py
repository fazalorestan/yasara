from pathlib import Path

def test_path_4():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/windows_artifact_registration/portable_zip_plan.py').exists()
