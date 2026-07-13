from pathlib import Path

def test_market_engine_router_script_exists():
    root = Path(__file__).resolve().parents[1]
    assert (root/'scripts'/'apply_v2_2_market_data_engine_router_patch.py').exists()
