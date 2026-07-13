from pathlib import Path

def test_v442_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_42_indicator_chart_integration_router_patch.py").exists()
