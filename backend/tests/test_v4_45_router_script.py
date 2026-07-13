from pathlib import Path

def test_v445_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_45_indicator_engine_bridge_router_patch.py").exists()
