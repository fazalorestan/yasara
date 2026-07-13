from pathlib import Path

def test_v500_alpha39_a_path_frontend():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/live-data/v5-live-data-core-types.ts').exists()
