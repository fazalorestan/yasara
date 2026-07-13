from pathlib import Path

def test_v49_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "marketStructure.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "MarketStructureStatus.tsx").exists()
