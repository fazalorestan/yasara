from pathlib import Path

def test_v425_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_25_policy_gate_router_patch.py").exists()
