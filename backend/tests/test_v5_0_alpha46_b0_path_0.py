from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_46/CORE_STABILIZATION_PACKAGE_B0.md').exists()
