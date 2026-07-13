from pathlib import Path

def test_v500_alpha1_frontend_contract():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'indicators'/'v5-indicator-plugin-contract.ts').exists()
