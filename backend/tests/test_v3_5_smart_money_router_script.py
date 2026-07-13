from pathlib import Path

def test_v35_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v3_5_smart_money_router_patch.py").exists()
