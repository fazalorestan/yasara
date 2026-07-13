from pathlib import Path

def test_v500_alpha32_frontend():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'optimizer-pro'/'v5-strategy-optimizer-pro-types.ts').exists()
