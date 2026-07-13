from pathlib import Path

def test_v34_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "marketAnalysis.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "MarketAnalysisStatus.tsx").exists()
