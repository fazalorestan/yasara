from pathlib import Path

def test_v500_alpha28_frontend_type():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'alerts'/'v5-alert-engine-types.ts').exists()
