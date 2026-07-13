from pathlib import Path

def test_v446_frontend_scanner_types():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "indicators" / "yasara" / "yasara-scanner-types.ts").exists()
