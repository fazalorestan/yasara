from pathlib import Path

def test_v410_router_script():
    root=Path(__file__).resolve().parents[1]; assert (root/'scripts'/'apply_v4_10_market_structure_sprint2_router_patch.py').exists()
