from pathlib import Path

def test_exchange_connector_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v2_3_exchange_connector_router_patch.py").exists()
