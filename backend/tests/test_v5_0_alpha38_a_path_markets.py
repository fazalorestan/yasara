from pathlib import Path

def test_v500_alpha38_a_path_markets():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/exchange_layer/markets.py').exists()
