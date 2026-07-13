from pathlib import Path

def test_v500_alpha30_frontend_type():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'replay'/'v5-replay-engine-types.ts').exists()
