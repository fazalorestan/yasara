from pathlib import Path

def test_path_13():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_2_ALPHA_FORCE_MERGE_K_SQLALCHEMY_GATE_CHANGELOG.md').exists()
