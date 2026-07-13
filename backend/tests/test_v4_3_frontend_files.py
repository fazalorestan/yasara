from pathlib import Path

def test_v43_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "riskEngine.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "RiskEngineStatus.tsx").exists()
