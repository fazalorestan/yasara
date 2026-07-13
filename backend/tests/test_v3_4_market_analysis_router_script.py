from pathlib import Path

def test_v34_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v3_4_market_analysis_router_patch.py").exists()
