from pathlib import Path

def test_v500_alpha38_c_path_frontend():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/exchange-layer/v5-exchange-connectivity-types.ts').exists()
