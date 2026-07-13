from pathlib import Path

def test_v424_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_24_plugin_registry_sync_router_patch.py").exists()
