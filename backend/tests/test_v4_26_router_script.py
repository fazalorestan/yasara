from pathlib import Path

def test_v426_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_26_platform_contracts_sdk_router_patch.py").exists()
