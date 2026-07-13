from pathlib import Path

def test_v500_alpha23_frontend_type():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'risk'/'v5-risk-engine-types.ts').exists()
