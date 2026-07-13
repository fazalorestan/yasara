from pathlib import Path

def test_v361_scripts():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v3_6_1_phase_a_guardrails_router_patch.py").exists()
    assert (root / "scripts" / "validate_v3_6_1_guardrails.py").exists()
