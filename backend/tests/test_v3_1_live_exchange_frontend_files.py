from pathlib import Path

def test_v31_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "liveExchange.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "LiveExchangeStatus.tsx").exists()
