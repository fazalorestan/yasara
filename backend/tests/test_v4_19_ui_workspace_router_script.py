from pathlib import Path

def test_v419_ui_workspace_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_19_ui_workspace_router_patch.py").exists()
