from pathlib import Path

def test_path_7():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/build_dashboard/artifact_signal_provider.py').exists()
