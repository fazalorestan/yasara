from pathlib import Path

def test_path_14():
 root=Path(__file__).resolve().parents[2]; assert (root/'scripts/register_windows_artifact.py').exists()
