from pathlib import Path

def test_path_1():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/project-intelligence/v5-pic-core-types.ts').exists()
