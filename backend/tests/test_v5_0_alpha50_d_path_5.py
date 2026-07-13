from pathlib import Path

def test_path_5():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/windows_artifact_registration/artifact_registry_update.py').exists()
