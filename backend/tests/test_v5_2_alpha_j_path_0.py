from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_2_alpha/AUTO_DEPENDENCY_DISCOVERY_EXECUTABLE_VALIDATION_PACKAGE_J.md').exists()
