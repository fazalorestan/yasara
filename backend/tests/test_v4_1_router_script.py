from pathlib import Path

def test_v41_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_1_indicator_engine_router_patch.py").exists()
