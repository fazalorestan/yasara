from pathlib import Path

def test_v500_alpha31_frontend_type():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'optimizer'/'v5-optimizer-types.ts').exists()
