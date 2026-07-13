from pathlib import Path

def test_v443_frontend_runtime_types():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "indicators" / "yasara" / "yasara-runtime-types.ts").exists()
