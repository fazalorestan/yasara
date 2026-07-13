from pathlib import Path

def test_v450_frontend_handoff_types():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "indicators" / "yasara" / "yasara-handoff-types.ts").exists()
