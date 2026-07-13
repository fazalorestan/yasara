from pathlib import Path

def test_v500_alpha38_b_path_metadata():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/exchange_layer/market_metadata.py').exists()
