from pathlib import Path

def test_v43_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_3_risk_engine_router_patch.py").exists()
