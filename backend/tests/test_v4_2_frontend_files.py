from pathlib import Path

def test_v42_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "signalEngine.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "SignalEngineStatus.tsx").exists()
