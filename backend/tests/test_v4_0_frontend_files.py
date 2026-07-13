from pathlib import Path

def test_v40_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "marketContext.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "MarketContextStatus.tsx").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "AutoTradeGateStatus.tsx").exists()
