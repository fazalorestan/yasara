from pathlib import Path
def test_v500_alpha11_frontend_type():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "licensing" / "v5-license-activation-types.ts").exists()
