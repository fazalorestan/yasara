from pathlib import Path

def test_v448_frontend_settings_types():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "indicators" / "yasara" / "yasara-settings-types.ts").exists()
