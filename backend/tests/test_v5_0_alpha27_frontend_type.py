from pathlib import Path

def test_v500_alpha27_frontend_type():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'scanner'/'v5-scanner-types.ts').exists()
