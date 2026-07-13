from pathlib import Path

def test_v410_frontend_files():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'api'/'marketStructureSprint2.ts').exists(); assert (root/'frontend'/'src'/'components'/'operational'/'MarketStructureSprint2Status.tsx').exists()
