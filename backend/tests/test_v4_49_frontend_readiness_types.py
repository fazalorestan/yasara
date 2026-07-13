from pathlib import Path

def test_v449_frontend_readiness_types():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "indicators" / "yasara" / "yasara-readiness-types.ts").exists()
