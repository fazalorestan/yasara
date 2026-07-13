from pathlib import Path

def test_v32_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v3_2_advanced_ai_indicators_router_patch.py").exists()
