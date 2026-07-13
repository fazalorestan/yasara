from pathlib import Path

def test_v500_alpha33_1_path_frontend():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/patching/v5-simple-patch-runner-types.ts').exists()
