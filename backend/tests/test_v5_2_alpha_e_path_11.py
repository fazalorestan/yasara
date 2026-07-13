from pathlib import Path

def test_path_11():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_2_ALPHA_EMBEDDED_BACKEND_BOOTSTRAP_CHANGELOG.md').exists()
