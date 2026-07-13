from pathlib import Path

def test_v46_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "tradingJournal.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "TradingJournalStatus.tsx").exists()
