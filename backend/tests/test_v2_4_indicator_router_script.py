from pathlib import Path

def test_indicator_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v2_4_indicator_signal_router_patch.py").exists()
