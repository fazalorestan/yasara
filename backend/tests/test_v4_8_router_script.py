from pathlib import Path

def test_v48_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_8_production_readiness_router_patch.py").exists()
