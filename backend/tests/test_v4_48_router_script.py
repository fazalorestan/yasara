from pathlib import Path

def test_v448_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_48_indicator_settings_presets_router_patch.py").exists()
