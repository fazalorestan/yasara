from pathlib import Path

def test_path_16():
 root=Path(__file__).resolve().parents[2]; assert (root/'packaging/windows/version_info.txt').exists()
