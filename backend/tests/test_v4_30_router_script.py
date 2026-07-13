from pathlib import Path

def test_v430_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_30_platform_diagnostics_router_patch.py").exists()
