from pathlib import Path

def test_path_14():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/production-runtime/v5-runtime-lifecycle-types.ts').exists()
