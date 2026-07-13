from pathlib import Path

def test_indicator_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "indicatorSignal.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "IndicatorSignalStatus.tsx").exists()
