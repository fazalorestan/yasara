from pathlib import Path
def test_v500_alpha18_frontend_type():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "exchanges" / "v5-exchange-sdk-types.ts").exists()
