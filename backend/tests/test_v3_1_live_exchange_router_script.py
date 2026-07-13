from pathlib import Path

def test_v31_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v3_1_live_exchange_router_patch.py").exists()
