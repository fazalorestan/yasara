from pathlib import Path

def test_v441_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_41_yasara_indicator_router_patch.py").exists()
