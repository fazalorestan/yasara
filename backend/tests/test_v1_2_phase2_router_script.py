from pathlib import Path
def test_market_workspace_router_script_exists():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v1_2_phase2_market_workspace_router_patch.py").exists()
