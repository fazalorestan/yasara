from pathlib import Path

def test_v49_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_9_market_structure_router_patch.py").exists()
