from pathlib import Path

def test_market_engine_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root/'frontend'/'src'/'api'/'marketEngine.ts').exists()
    assert (root/'frontend'/'src'/'components'/'operational'/'MarketEngineStatus.tsx').exists()
