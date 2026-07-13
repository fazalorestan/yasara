from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_2_alpha/CRYPTOGRAPHY_RUNTIME_DEPENDENCY_FIX_PACKAGE_I.md').exists()
