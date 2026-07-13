from pathlib import Path

def test_v441_frontend_indicator_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "indicators" / "yasara" / "yasara-script.ts").exists()
    assert (root / "frontend" / "src" / "indicators" / "indicator-registry.ts").exists()
