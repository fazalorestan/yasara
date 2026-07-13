from pathlib import Path

def test_path_17():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_46_CORE_STABILIZATION_CHANGELOG.md').exists()
