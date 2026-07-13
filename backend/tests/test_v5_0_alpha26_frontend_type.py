from pathlib import Path

def test_v500_alpha26_frontend_type():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'portfolio'/'v5-portfolio-manager-types.ts').exists()
