from pathlib import Path
def test_workspace_polish_router_script_exists():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v1_2_6_workspace_polish_router_patch.py").exists()
