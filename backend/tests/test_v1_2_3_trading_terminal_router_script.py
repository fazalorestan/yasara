from pathlib import Path
def test_trading_terminal_router_script_exists():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v1_2_3_milestone1_trading_terminal_router_patch.py").exists()
