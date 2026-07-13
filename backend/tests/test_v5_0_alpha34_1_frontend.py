from pathlib import Path

def test_v500_alpha34_1_frontend():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'router'/'v5-router-proof-types.ts').exists()
