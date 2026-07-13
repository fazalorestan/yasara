from pathlib import Path

def test_v423_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_23_plugin_catalog_router_patch.py").exists()
