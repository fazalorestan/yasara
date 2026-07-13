from pathlib import Path

def test_v500_alpha38_b_path_frontend():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/exchange-layer/v5-exchange-market-data-types.ts').exists()
