from pathlib import Path

def test_v500_alpha29_frontend_type():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'backtest'/'v5-backtest-engine-types.ts').exists()
