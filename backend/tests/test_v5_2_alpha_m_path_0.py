from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_2_alpha/APSCHEDULER_DEPENDENCY_GATE_LEGACY_J_TEST_FIX_PACKAGE_M.md').exists()
