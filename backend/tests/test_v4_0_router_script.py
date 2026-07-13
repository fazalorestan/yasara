from pathlib import Path

def test_v40_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_0_market_context_router_patch.py").exists()
