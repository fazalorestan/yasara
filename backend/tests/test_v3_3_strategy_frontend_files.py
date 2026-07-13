from pathlib import Path

def test_v33_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "strategyBuilder.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "StrategyBuilderStatus.tsx").exists()
