from pathlib import Path

def test_path_14():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_2_ALPHA_LEGACY_MARKER_LAUNCHER_SYNC_DIAGNOSTICS_CHANGELOG.md').exists()
