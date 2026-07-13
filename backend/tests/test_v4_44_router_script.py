from pathlib import Path

def test_v444_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_44_indicator_pine_source_router_patch.py").exists()
