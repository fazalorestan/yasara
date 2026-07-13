from pathlib import Path

def test_v436_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_36_enterprise_scheduler_router_patch.py").exists()
