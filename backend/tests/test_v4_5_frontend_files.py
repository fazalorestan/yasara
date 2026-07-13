from pathlib import Path

def test_v45_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "paperTradingV45.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "PaperTradingV45Status.tsx").exists()
