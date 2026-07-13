from pathlib import Path

def test_v25_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v2_5_risk_backtest_paper_router_patch.py").exists()
