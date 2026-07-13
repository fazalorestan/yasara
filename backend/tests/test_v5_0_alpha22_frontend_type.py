from pathlib import Path

def test_v500_alpha22_frontend_type():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'broker'/'v5-broker-layer-types.ts').exists()
