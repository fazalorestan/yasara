from pathlib import Path

def test_v45_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_5_paper_trading_router_patch.py").exists()
