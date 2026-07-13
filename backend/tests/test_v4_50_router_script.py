from pathlib import Path

def test_v450_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_50_indicator_platform_handoff_router_patch.py").exists()
