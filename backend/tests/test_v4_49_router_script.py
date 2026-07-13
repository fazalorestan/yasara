from pathlib import Path

def test_v449_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_49_indicator_final_readiness_router_patch.py").exists()
