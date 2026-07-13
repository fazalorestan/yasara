from pathlib import Path

def test_v41_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "indicatorEngine.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "IndicatorEngineStatus.tsx").exists()
