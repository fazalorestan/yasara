from pathlib import Path

def test_path_15():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_49_DESKTOP_FINALIZATION_CHANGELOG.md').exists()
