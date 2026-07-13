from pathlib import Path

def test_v500_alpha37_b_path_frontend2():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/broker-layer/v5-broker-orders-account-types.ts').exists()
