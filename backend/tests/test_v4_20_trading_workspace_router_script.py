from pathlib import Path

def test_v420_trading_workspace_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_20_trading_workspace_router_patch.py").exists()
