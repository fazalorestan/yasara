from pathlib import Path

def test_path_2():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_44/PROJECT_INTELLIGENCE_CENTER_PACKAGE_A.md').exists()
