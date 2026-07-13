from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_2_alpha/FORCE_MERGE_K_LEGACY_TEST_SQLALCHEMY_GATE_PACKAGE_L.md').exists()
