from pathlib import Path

def test_path_21():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/build-pipeline/v5-build-pipeline-types.ts').exists()
