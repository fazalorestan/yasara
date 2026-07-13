from pathlib import Path

def test_v33_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v3_3_strategy_builder_router_patch.py").exists()
