from pathlib import Path

def test_v500_alpha38_b_path_candles():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/exchange_layer/candles.py').exists()
