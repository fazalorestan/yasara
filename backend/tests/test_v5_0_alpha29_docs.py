from pathlib import Path

def test_v500_alpha29_docs():
    root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_29'/'BACKTEST_ENGINE_FOUNDATION.md').exists()
