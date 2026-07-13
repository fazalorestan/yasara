from pathlib import Path

def test_v500_alpha26_docs():
    root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_26'/'PORTFOLIO_MANAGER_FOUNDATION.md').exists()
