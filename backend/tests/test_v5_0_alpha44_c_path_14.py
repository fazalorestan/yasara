from pathlib import Path

def test_path_14():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/project-intelligence/v5-build-intelligence-types.ts').exists()
