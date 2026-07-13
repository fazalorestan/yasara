from pathlib import Path

def test_v500_alpha20_frontend_type():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'api-search'/'v5-api-search-types.ts').exists()
