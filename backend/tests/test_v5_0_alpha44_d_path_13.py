from pathlib import Path

def test_path_13():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/project-intelligence/v5-desktop-dashboard-types.ts').exists()
