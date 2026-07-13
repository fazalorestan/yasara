from pathlib import Path
def test_portfolio_orders_router_script_exists():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v1_2_4_milestone2_portfolio_orders_router_patch.py").exists()
