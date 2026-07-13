from pathlib import Path

def test_path_8():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/legacy_marker_launcher_sync_diagnostics/readiness.py').exists()
