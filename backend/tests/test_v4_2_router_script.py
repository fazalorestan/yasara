from pathlib import Path

def test_v42_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_2_signal_engine_router_patch.py").exists()
