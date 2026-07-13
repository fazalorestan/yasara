from pathlib import Path

def test_v500_alpha19_frontend_type():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'api-routing'/'v5-auto-router-types.ts').exists()
