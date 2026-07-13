from pathlib import Path

def test_v500_alpha41_d_path_frontend():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/strategy-engine/v5-strategy-simulation-types.ts').exists()
