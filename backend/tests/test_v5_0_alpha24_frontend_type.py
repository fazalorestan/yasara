from pathlib import Path

def test_v500_alpha24_frontend_type():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'api-smoke'/'v5-runtime-api-smoke-types.ts').exists()
