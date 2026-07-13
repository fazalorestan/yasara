from pathlib import Path

def test_v44_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "backtestBenchmark.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "BacktestBenchmarkStatus.tsx").exists()
