from pathlib import Path

def test_v500_alpha30_1_frontend_type():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'router'/'v5-router-auto-registration-types.ts').exists()
