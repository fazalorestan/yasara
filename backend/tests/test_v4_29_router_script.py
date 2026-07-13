from pathlib import Path

def test_v429_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_29_timezone_runtime_router_patch.py").exists()
