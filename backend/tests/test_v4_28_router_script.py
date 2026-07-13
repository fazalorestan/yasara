from pathlib import Path

def test_v428_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_28_plugin_state_snapshot_router_patch.py").exists()
