from pathlib import Path

def test_v444_frontend_pine_file():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "indicators" / "yasara" / "pine" / "yasara-v1.pine").exists()
