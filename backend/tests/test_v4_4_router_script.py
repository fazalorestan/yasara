from pathlib import Path

def test_v44_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_4_backtest_benchmark_router_patch.py").exists()
