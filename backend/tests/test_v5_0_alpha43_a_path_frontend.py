from pathlib import Path

def test_v500_alpha43_a_path_frontend():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/broker-layer/v5-broker-core-types.ts').exists()
