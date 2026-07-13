from pathlib import Path

def test_path_13():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/project-intelligence/v5-pic-enterprise-types.ts').exists()
