from pathlib import Path

def test_v26_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "finalOperational.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "FinalOperationalStatus.tsx").exists()
