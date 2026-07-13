from pathlib import Path

def test_v500_alpha34_0_path_frontend():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/router/v5-auto-router-registry-types.ts').exists()
