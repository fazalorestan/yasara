from pathlib import Path

def test_v443_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_43_indicator_runtime_adapter_router_patch.py").exists()
