from pathlib import Path

def test_v500_alpha21_frontend_type():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'patching'/'v5-patch-pipeline-types.ts').exists()
