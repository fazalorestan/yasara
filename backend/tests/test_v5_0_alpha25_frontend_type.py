from pathlib import Path

def test_v500_alpha25_frontend_type():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'patching'/'v5-self-healing-patch-types.ts').exists()
